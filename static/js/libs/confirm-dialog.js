YUI.add('confirmDialog', function (Y) {
 
 /* Fix Me this has to be implement for App.Right now it's only for PDF */

 Y.ConfirmDialog = function(cfg){
	  
  	var text = cfg.text,
  		yes_button = cfg.buttons[0].text;
  		no_button = cfg.buttons[1].text;
  		style = cfg.style;
	var node = Y.Node.create('<div class="modal modal_css" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">'
				+	'<div class="modal-header">'
				+ 		'<p>'+text+'</p>'
				+	'</div>'
				+	'<div class="modal-footer">'
				+		(cfg.cancel ? '<button class="btn btn-cancel" tabindex="0"> Cancel </button>' : '')
				+       '<button class="btn btn-yes" tabindex="0">'+ yes_button +'</button>'
				+		'<button class="btn btn-no" tabindex="0">'+ no_button +'</button>'
				+	'</div>'
			+'</div>'), 
		backdrop = Y.Node.create('<div class="modal-backdrop fade in"></div>'),
		body = Y.one('body');
	  backdrop.addClass(style);
	body.append(backdrop,'after')
		.append(node,'after');
		
	var btnY = node.one('.btn-yes'), btnN = node.one('.btn-no');
	
	var tabHandler = body.on('keydown', function(e){
		// Handle Tabs in a custom manner
		if ( e.keyCode == 9 || // Tab 
				e.keyCode == 37 || e.keyCode == 39 || // Left / Right 
					e.keyCode == 33 || e.keyCode == 34 || // Page-up / Page Down
						e.keyCode == 38 || e.keyCode == 40) // Up / Down
		{ 
			e.halt();
			if ( btnY.hasClass('btn-primary')) {
				btnN.addClass('btn-primary').focus();
				btnY.removeClass('btn-primary');
			} else {
				btnY.addClass('btn-primary').focus();
				btnN.removeClass('btn-primary');
			}
		} else if ( e.keyCode == 27){
			// Escape is like clicking No
			e.halt();
			cfg.flag? btnY.simulate('click'): btnN.simulate('click');
		}
		
	});
	
	cfg.flag ? btnY.focus().addClass('btn-primary'): btnN.focus().addClass('btn-primary');
	
	node.delegate('click', function(e){
		node.remove();
		backdrop.remove();
		tabHandler.detach();
		
		if ( cfg.buttons[0].onclick ) {
			cfg.buttons[0].onclick();	
		}
		
	}, '.btn-yes');
	
	node.delegate('click', function(e){
		node.remove();
		backdrop.remove();
		tabHandler.detach();
		if(typeof(cfg.cancel) == "function"){
			cfg.cancel();	
		}
		
	}, '.btn-cancel');
	
	
	node.delegate('click', function(e){
		node.remove();
		backdrop.remove();
		tabHandler.detach();
		
		if ( cfg.buttons[1].onclick ){
			cfg.buttons[1].onclick();	
		}
		
	}, '.btn-no');
},
Y.namespace('Plugin'); // add this plugin to Y.Plugin namspace
}, "3.1.0", {
  requires: ["plugin","node","node-event-simulate"]
});
