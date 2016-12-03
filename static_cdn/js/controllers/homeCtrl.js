app = angular.module('homeCtrl', []);

app.controller('homeController',function(Video_links,$scope) {

//List All Videos//

    Video_links.all()
        .success(function(data){

            $scope.videos = data;

            $scope.getIframeSrc = function (videoId) {
                return 'https://www.youtube.com/embed/' + videoId;
            };        
        });

 
});
