app
// =========================================================================
// Show View and Delete medicamento 
// =========================================================================
    .controller("DerivacionCtrl", function($scope, $state, $stateParams, topico2Service, $window, $mdDialog, $log, toastr) {
    //Valores iniciales
    $scope.fields = 'name,codename';
    var params = {};
    $scope.lista = [];
    $scope.derivacion = {};

    
    //$window.location = "#" + $location.path();

    $scope.list = function(params) {
        $scope.isLoading = true;
        topico2Service.Derivacion.query(params, function(r) {
            $scope.lista = r;
            //$scope.options = r.options;
            $scope.isLoading = false;
        }, function(err) {
            $log.log("Error in list:" + JSON.stringify(err));
            toastr.error(err.data.results.detail, err.status + ' ' + err.statusText);
        });
    };
    $scope.list(params);

    $scope.buscar = function() {
        params.page = 1;
        params.fields = $scope.fields;
        params.query = $scope.query;
        $scope.list(params);
    };

    $scope.onReorder = function(order) { //TODO
        $log.log('Order: ' + order);
    };

    $scope.delete = function(d) {
        if ($window.confirm("Seguro?")) {
            topico2Service.Derivacion.delete({ id: d.id }, function(r) {
                $log.log("Se eliminó la derivacion:" + JSON.stringify(d));
                toastr.success('Se eliminó la derivacion ' + d.nombre, 'derivacion');
                $scope.list(params);
            }, function(err) {
                $log.log("Error in delete:" + JSON.stringify(err));
                toastr.error(err.data.detail, err.status + ' ' + err.statusText);
            });
        }
    };

})

// =========================================================================
// Create and Update medicamento
// =========================================================================
.controller("DerivacionSaveCtrl", function($scope, $state, $stateParams, topico2Service, $window, $mdDialog, $log, toastr) {
    //Valores iniciales
    $scope.derivacion = {};

    $scope.sel = function() {
        topico2Service.Derivacion.get({ id: $stateParams.id }, function(r) {
            $scope.derivacion = r;
        }, function(err) {
            $log.log("Error in get:" + JSON.stringify(err));
            toastr.error(err.data.detail, err.status + ' ' + err.statusText);
        });
    };
    if ($stateParams.id) {
        $scope.sel();
    }

    $scope.save = function() {
        if ($scope.derivacion.id) {
            topico2Service.Derivacion.update({ id: $scope.derivacion.id }, $scope.derivacion, function(r) {
                $log.log("r: " + JSON.stringify(r));
                toastr.success('Se editó la derivacion ' + r.enfermedadactual, 'derivacion');
                $state.go('topico2.topico2.derivacions');
            }, function(err) {
                $log.log("Error in update:" + JSON.stringify(err));
                toastr.error(err.data.detail, err.status + ' ' + err.statusText);
            });
        } else {
            topico2Service.Derivacion.save($scope.derivacion, function(r) {
                $log.log("r: " + JSON.stringify(r));
                toastr.success('Se insertó la derivacion ' + r.enfermedadactual, 'derivacion');
                $state.go('topico2.topico2.derivacions');
            }, function(err) {
                $log.log("Error in save:" + JSON.stringify(err));
                toastr.error(err.data.detail, err.status + ' ' + err.statusText);
            });
        }
    };

    $scope.cancel = function() {
        $state.go('topico2.topico2.derivacions');
    };
});
