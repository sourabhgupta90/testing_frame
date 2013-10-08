/*
    This plugin will be used to auto-resize the text-area vertically, while text is enterd,
    uptil a max-height and then a scroll will be added. We can specify the min & max height
    either by css-style or by providing a config attribute while pluging in target node.
    
    Priority for configuration will be in order-
    1. css-style - highest priority.
    2. configuration attribute provided during pluging.
    3. default configuration if none is provided.(min-height:30px,max-height:100px)
*/
YUI.add('resizeTextAreaPlugin', function (Y) { // implement as module 

  var copy = Y.Node.create('<div id="copytextarea" \
                              style="visibility:hidden;">\
                              </div>');
  Y.one('body').append(copy);

  function ResizeTextArea(config) {
    ResizeTextArea.superclass.constructor.apply(this, arguments);
  }

  ResizeTextArea.Name = "resizeTextArea";
  ResizeTextArea.NS = "resize";
  ResizeTextArea.ATTRS = { // default configuration
    maxHeight: {
      value: "100px"
    },
    minHeight: {
      value: "30px"
    }
  };

  Y.extend(ResizeTextArea, Y.Plugin.Base, {

    initializer: function (cfg) {
      this.host = this.get("host"); // the node that use this plugin
      this.onHostEvent(["keyup", "keydown"], this._autoResize); // listen the host event
                    
      this._setMinMaxHeight(cfg); // set configuration a/c priority
    },
    destructor: function () {},

    _setMinMaxHeight: function (cfg) {

      (parseInt(this.host.getStyle('minHeight')) && this.set('minHeight', this.host.getStyle('minHeight'))) || (parseInt(cfg.minHeight) && this.set('minHeight', cfg.minHeight));
      (parseInt(this.host.getStyle('maxHeight')) && this.set('maxHeight', this.host.getStyle('maxHeight'))) || (parseInt(cfg.maxHeight) && this.set('maxHeight', cfg.maxHeight));
      this.host.setStyles({'min-height':this.get('minHeight'),'max-height':this.get('maxHeight')});      
    },

    _setStyle: function (node) {
      copy.setStyles({
        'font-family': node.getStyle('fontFamily'),
        'font-size': node.getStyle('fontSize'),
        'padding': node.getStyle('padding'),
        'padding-left': node.getStyle('paddingLeft'),
        'padding-right': node.getStyle('paddingRight'),
        'padding-top': node.getStyle('paddingTop'),
        'padding-bottom': node.getStyle('paddingBottom'),
        'width': node.getStyle('width'),
        'word-wrap': 'break-word'
      });
    },
    _autoResize: function (e) {

      var node = e.currentTarget;
      this._setStyle(node);
      node.setStyle('overflow', 'hidden');
      var text = node.get('value').replace(/\n/g, '<br/>');
      copy.set('innerHTML', text + '<br />');
      var newHeight = parseInt(copy.getStyle('height')),
        minHeight = parseInt(this.get('minHeight')),
        maxHeight = parseInt(this.get('maxHeight'));

      copy.set('innerHTML', '');

      if (newHeight <= maxHeight) {
        node.setStyle('height', newHeight);
      }
      var overflowY = newHeight > maxHeight ? 'scroll' : 'hidden';
      node.setStyle('overflow-y', overflowY);
    }
  });
  Y.namespace('Plugin'); // add this plugin to Y.Plugin namspace
  Y.Plugin.ResizeTextArea = ResizeTextArea;

}, "3.1.0", {
  requires: ["plugin","node"]
});
