;
var CoverageApp = function () {

    var self = this;
    this.debug = true;
    this.is_fs = false;

    this.init = function () {
        self.bindings();
    };

    this.bindings = function () {

        $(document).on('click', '[data-map-toggle-fs]', function(e){
            self.is_fs = !self.is_fs;
            var container = $(this).parents('.coverage-map');
            if(self.is_fs) {
                container.addClass('fullscreen');
                $('body').addClass('fullscreen-map');

            } else {
                container.removeClass('fullscreen');
                $('body').removeClass('fullscreen-map');
            }
        });
        
    };

};