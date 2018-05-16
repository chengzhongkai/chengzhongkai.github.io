_marked = marked

marked = function(src, opt, callback){
	var PREFIX = "<script type=\"math/tex\">";
    var SUFFIX = "</script>";
    var reg = new RegExp(
      ("(?:" + PREFIX + "([\\s\\S]*?)" + SUFFIX + ")")
        .replace(/\//g, "\/"),
      "gm");
    var wraped = src.split("$$")
      .reduce(function(sum, str, i){
        return i % 2 === 0 ?
               sum + str :
               sum + PREFIX + str + SUFFIX;
      }, "");
    var html = _marked(wraped, opt, callback)
    
    return html;

}