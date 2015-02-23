;
AchatApp = function () {

    var self = this;
    this.debug = false;
    this.container;
    this.user;
    this.messages_container;
    this.max_messages = 24;

    this.init = function () {

        if(self.debug) {
            debug.debug('AchatApp: init');
        }
        self.messages_container = $('.messages-container', self.container);
        self.bindings();

        pushy_client.subscribe('achat', function(message){
            self.add_message(message);
        });

    };


    this.bindings = function () {



        self.container.on('click', 'a[data-action="submit"]', function (e) {
            e.preventDefault();
            // don't act on 'span' click (used to toggle dropdown)
            if(! $(e.toElement).is('span')) {
                var options = {
                    extra: $(this).data('message_extra') || false
                };
                self.create_message($('.chat-message', self.container).html(), options)
            }
        });


        self.container.on('submit', 'form', function (e) {

            e.preventDefault();
            self.create_message($('.chat-message', self.container).html())

        });


        self.container.on('keydown', '.chat-message > p', function (e) {
            e = e || event;
            if (e.keyCode === 13 && !e.shiftKey) {
                $('form', self.container).submit();
                e.preventDefault();
                return false;
            }
            return true;

        });

        // show all text in case that truncated
        self.messages_container.on('click', 'a.show-full-text', function(e){
            e.preventDefault();
            var message_body = $(this).parents('.body');
            $('.truncated', message_body).toggle();
            $('.full', message_body).toggle();
        });

        self.container.on('focus', '.chat-message > p', function (e) {
            $(this).parents('form').addClass('focus');
        });
        self.container.on('blur', '.chat-message > p', function (e) {
            $(this).parents('form').removeClass('focus');
        });

        // user login/logout handling
        $(document).on('alogin', function(e, type, user){
            if(type == 'auth-state-change') {
                if(user != undefined) {
                    self.user = user;
                    // reload chat messages
                    self.messages_container.html('')
                    self.load();
                }
            }
        });


        $('span.timestamp', self.messages_container).timeago();



        var strategies = [
            { // mention strategy
                match: /(^|\s)@(\w*)$/,
                search: function (term, callback) {
                    //callback(cache[term], true);
                    $.getJSON('/api/v1/auth/user/', { username__icontains: term })
                        .done(function (resp) {
                            //console.log(resp.objects)
                            callback(resp.objects);
                        })
                        .fail(function () {
                            callback([]);
                        });
                },
                template: function (value) {

                    return value.username + ' | ' + value.email;
                },
                replace: function (value) {
                    console.log(value)
                    //return '$1<a href="#">' + value.username + '</a>   ';
                    return '$1<span data-ct="user">' + '@' + value.username + '</span>   ';
                    //return '$1@:' + value.username + ': ';
                },
                cache: true
            },
            { // mention strategy
                match: /(^|\s)#(\w*)$/,
                search: function (term, callback) {
                    //callback(cache[term], true);
                    $.getJSON('/lsearch', { q: term })
                        .done(function (resp) {
                            console.log(resp)
                            callback(resp.objects);
                        })
                        .fail(function () {
                            callback([]);
                        });
                },
                replace: function (value) {
                    return '$1@' + value + ' ';
                },
                cache: true
            }
        ]
        var option = {
            appendTo: $('body')
        };


        $('#chat_input', self.container).textcomplete(strategies, option);


    };


    this.create_message = function (text, options) {

        if ($(text).html().length > 2) {

            var data = JSON.stringify({
                "text": $(text).html(),
                "options": options
            });

            $.ajax({
                url: '/api/v1/chat/message/',
                type: 'POST',
                contentType: 'application/json',
                data: data,
                dataType: 'json',
                processData: false
            })

        }
        $('.chat-message > p', self.container).html('')


    };

    this.load = function () {
        var url = '/api/v1/chat/message/' + '?limit=' + self.max_messages;
        $.get(url, function (data) {
            $.each(data.objects.reverse(), function (i, message) {
                self.add_message(message);
            });
        });

    };

    // TODO: seems not to be needed anymore
    this.push_message = function (message) {
        self.add_message(message);
    };

    this.add_message = function (message) {

        if(self.debug) {
            debug.debug('AchatApp: add_message', message);
        }

        // fix some values
        //message.created = message.created.substr(11, 8);
        if (self.user && message.user.id == self.user.id) {
            message.user.is_me = true;
        }

        if (message.options && message.options.extra ) {
            message.extra_classes = message.options.extra
        }

        var html = $(nj.render('achat/nj/message.html', {message: message}));
        setTimeout(function () {
            html.removeClass('new');
        }, 100)

        self.messages_container.prepend(html);
        self.messages_container.find('.item.message:gt(' + self.max_messages + ')').remove()


        // 'dynamic' timestamps
        $('span.timestamp', self.messages_container).timeago('updateFromDOM');


    };

};

