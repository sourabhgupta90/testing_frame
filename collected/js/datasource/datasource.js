YUI().use("datasource",'node', 'event','autocomplete', 'autocomplete-highlighters', function (Y) {
            var myDataSource = new Y.DataSource.Get({
                source: "/datasource_data/"
            });
            
            var myDataSource12 = new Y.DataSource.Function({
                source: function (request) {
                    return [["ann", 123], ["bill", 456]];
                }
            });
            Y.one('body').addClass('yui3-skin-sam');    
            Y.one('.auto_complete_input').plug(Y.Plugin.AutoComplete, {render: false});

             var button = Y.one("#efficiency_button");
            
             button.on('click', function (e) {
                Y.one('.auto_complete_input').ac.render();    
                Y.one('.auto_complete_input').plug(Y.Plugin.AutoComplete, {
                    resultHighlighter: 'phraseMatch',
                    source: ['foo', 'bar', 'baz']
                 });
             });
        });
