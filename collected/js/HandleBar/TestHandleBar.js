var source   = $("#entry-template").html();
var template = Handlebars.compile(source);
var context = {"title": "My New Post", "body": "This is my first post!"};
var html = template(context);
$(".first").html(html);
