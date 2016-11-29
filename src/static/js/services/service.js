var app = angular.module('contactService', []);

app.factory('Contacts', function($http) {

    var contactFactory = {}; 

    contactFactory.create = function(contactData){
        return $http.post('/api/contacts/create/', contactData);

    };

    return contactFactory;

});

app.factory('Video_links', function($http) {

    var video_linkFactory = {}; 

    video_linkFactory.all = function(data){
        return $http.get('/api/contacts/video_links');
    };

    return video_linkFactory;

});

app.factory('Products', function($http) {

    var productFactory = {}; 

    productFactory.all = function(data){
        return $http.get('/api/contacts/products');
    };

    return productFactory;

});

