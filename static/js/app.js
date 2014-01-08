var app = YUI.use('app',function(Y){
   var app = Y.app({
       
   });
   app.route('/', function(){
       Y.one('h1').set('text','Stored Links');
   }); 
   app.render().dispatch();
});
