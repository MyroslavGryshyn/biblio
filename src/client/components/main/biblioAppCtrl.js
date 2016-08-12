'use strict';

angular.module('biblioApp').
    controller('biblioAppCtrl', ['$state', function ($state) {
        var vm = this;
        vm.openState = function(name) {
            // debugger
            $state.go(name);
        }
    }]);