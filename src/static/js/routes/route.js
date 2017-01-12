app = angular.module('indexRoute', ['ui.router']);

app.config(function($locationProvider, $stateProvider, $urlRouterProvider){
    $stateProvider
        .state('index',{
            url:'/',
            templateUrl: 'static/templates/home.html'
        })
        .state('contact',{
            url:'/contact',
            templateUrl: 'static/templates/contact.html'
        })
        .state('about',{
            url:'/about',
            templateUrl: 'static/templates/about.html'
        })
         .state('shop',{
            url:'/shop',
            templateUrl: 'static/templates/shop.html'
        })
        .state('product', {
            url:'/shop/:id',
            templateUrl : 'static/templates/product.html'
        })
        .state("otherwise",{ 
            url : '/',
            templateUrl: 'static/templates/home.html'
        });

    $locationProvider.html5Mode(true);
});

