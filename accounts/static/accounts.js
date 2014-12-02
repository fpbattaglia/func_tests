/**
 * Created by fpbatta on 02/12/2014.
 */

var initialize = function(navigator) {
    $('#id_login').on('click', function() {
        navigator.id.request();
    });
};

window.Superlists = {
    Accounts: {
        initialize: initialize
    }
};

