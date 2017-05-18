(function() {
    'use strict';

    openerp.website.if_dom_contains('.o_my_show_more', function() {

        $('.o_my_show_more').on('click', function(ev) {
            ev.preventDefault();
            $(this).parents('table').find(".to_hide").toggleClass('hidden');
            $(this).find('span').toggleClass('hidden');
        });

        var showMoreElement = document.querySelector('.o_my_show_more');
        showMoreElement.addEventListener('click', function (event) {
            event.preventDefault()
            document.querySelector('table .to_hide').classList.toggle('o_my_show_more')
            this.querySelector('span').classList.toggle('hidden')
        }, false )
    });

}());
