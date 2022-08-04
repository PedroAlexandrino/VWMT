(function($) {
    showTestToast = function(x) {
        'use strict';
        resetToastPosition();
        $.toast({
            heading: 'Success', // Optional heading to be shown on the toast
            text: 'Sucess', // Text that is to be shown in the toast
            icon: 'success', // Type of toast icon
            showHideTransition: 'fade', // fade, slide or plain
            allowToastClose: true, // Boolean value true or false
            hideAfter: 2000, // false to make it sticky or number representing the miliseconds as time after which toast needs to be hidden
            stack: 9, // false if there should be only one toast at a time or a number representing the maximum number of toasts to be shown at a time
            position: 'bottom-left', // bottom-left or bottom-right or bottom-center or top-left or top-right or top-center or mid-center or an object representing the left, right, top, bottom values
            textAlign: 'left', // Text alignment i.e. left, right or center
            loader: true, // Whether to show loader or not. True by default
            loaderBg: '#f96868', // Background color of the toast loader
            beforeShow: function() {}, // will be triggered before the toast is shown
            afterShown: function() {}, // will be triggered after the toat has been shown
            beforeHide: function() {}, // will be triggered before the toast gets hidden
            afterHidden: function() {} // will be triggered after the toast has been hidden
        });
    };
    showSuccessToast = function() {
        'use strict';
        resetToastPosition();
        $.toast({
            heading: 'Success',
            text: 'Esta é uma mensagem de sucesso, no modo de developer @Visteon',
            showHideTransition: 'slide',
            icon: 'success',
            loaderBg: '#f96868',
            position: 'top-right',
            hideAfter: 'false'
        })
    };
    showInfoToast = function() {
        'use strict';
        resetToastPosition();
        $.toast({
            heading: 'Info',
            text: 'And these were just the basic demos! Scroll down to check further details on how to customize the output.',
            showHideTransition: 'slide',
            icon: 'info',
            loaderBg: '#46c35f',
            position: 'top-right'
        })
    };
    showWarningToast = function() {
        'use strict';
        resetToastPosition();
        $.toast({
            heading: 'Warning',
            text: 'And these were just the basic demos! Scroll down to check further details on how to customize the output.',
            showHideTransition: 'slide',
            icon: 'warning',
            loaderBg: '#57c7d4',
            position: 'top-right'
        })
    };
    showDangerToast = function() {
        'use strict';
        resetToastPosition();
        $.toast({
            heading: 'Erro!',
            text: 'Existe um erro no seu pedido. Por favor verifique os dados novamente.',
            showHideTransition: 'slide',
            icon: 'error',
            loaderBg: '#f2a654',
            position: 'top-right'
        })
    };
    showPedidoToast = function() {
        'use strict';
        resetToastPosition();
        $.toast({
            heading: 'Feito!',
            text: 'Acção foi executada com sucesso!',
            showHideTransition: 'slide',
            icon: 'success',
            loaderBg: '#f2a654',
            position: 'top-right'
        })
    };
    ShowQtyError = function() {
        'use strict';
        resetToastPosition();
        $.toast({
            heading: 'Erro!',
            text: 'A quantidade introduzida não é válida.',
            showHideTransition: 'slide',
            icon: 'error',
            loaderBg: '#00ffd9',
            position: 'top-right'
        })
    };
    showReposicaoToast = function() {
        'use strict';
        resetToastPosition();
        $.toast({
            heading: 'Info',
            text: 'And these were just the basic demos! Scroll down to check further details on how to customize the output.',
            showHideTransition: 'slide',
            icon: 'info',
            loaderBg: '#46c35f',
            position: 'top-right'
        })
    };
    showRemoveToast = function() {
        'use strict';
        resetToastPosition();
        $.toast({
            heading: 'Danger',
            text: 'Artigo removido com sucesso!',
            showHideTransition: 'slide',
            hideAfter: 3000,
            icon: 'error',
            loaderBg: '#f2a654',
            position: 'bottom-right'
        })
    };
    showToastPosition = function(position) {
        'use strict';
        resetToastPosition();
        $.toast({
            heading: 'Positioning',
            text: 'Specify the custom position object or use one of the predefined ones',
            position: String(position),
            icon: 'success',
            stack: false,
            loaderBg: '#f96868'
        })
    }
    showToastInCustomPosition = function() {
        'use strict';
        resetToastPosition();
        $.toast({
            heading: 'Custom positioning',
            text: 'Specify the custom position object or use one of the predefined ones',
            icon: 'success',
            position: {
                left: 320,
                top: 120
            },
            stack: false,
            loaderBg: '#f96868'
        })
    }

    showGravarPosicao = function() {
        'use strict';
        resetToastPosition();
        $.toast({
            heading: 'Nota:',
            text: 'Se fizer alterações, não se esqueça de gravar a tabela.',
            icon: 'Info',
            hideAfter: 3000,
            position: {
                left: 155,
                top: 45
            },
            stack: false,
            loaderBg: '#f96868'
        })
    }
    resetToastPosition = function() {
        $('.jq-toast-wrap').removeClass('bottom-left bottom-right top-left top-right mid-center'); // to remove previous position class
        $(".jq-toast-wrap").css({
            "top": "",
            "left": "",
            "bottom": "",
            "right": ""
        }); //to remove previous position style
    }
})(jQuery);