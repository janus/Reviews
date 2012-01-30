      tinyMCE.init({
        theme : "advanced",
        plugins: " spellchecker,insertdatetime,tabfocus",
     theme_advanced_buttons1_add : "undo, redo, insertdate,forecolor,backcolor, outdent, indent, bullist, hr, strikethrough,spellchecker",
        theme_advanced_buttons2 : "",
        theme_advanced_buttons3 : "",
    plugin_insertdate_dateFormat : "%Y-%m-%d",
     theme_advanced_disable: "image, help, code, charmap, cut, styleselect,numlist,paste, fontselect, visualaid, removeformat, cleanup, anchor, unlink ,link ,newdocument,separator,sub,sup",
        theme_advanced_toolbar_location : "top",
        theme_advanced_toolbar_align : "left",
        mode : "exact",
        elements : "articleContent"
      });