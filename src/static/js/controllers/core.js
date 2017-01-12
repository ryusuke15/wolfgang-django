var WolfgangApp = angular.module('Wolfgang', [
    'indexRoute',
    'contactService',
    'contactCtrl',
    'homeCtrl',
    'shopCtrl',
    'productCtrl',    
]);

WolfgangApp.config([
    '$httpProvider','$interpolateProvider','$sceDelegateProvider', function($httpProvider, $interpolateProvider, $sceDelegateProvider){
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $httpProvider.defaults.headers.common["X-CSRFToken"] = window.csrf_token;

        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');

        $sceDelegateProvider.resourceUrlWhitelist([
            'self',
            'https://www.youtube.com/**'
      ]);

    }

]);
