<!DOCTYPE html>
<!-- saved from url=(0066)http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3 -->
<html lang="en-us"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    

    <title>Untitled - Jupyter Notebook</title>
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="./Assignment Day1_files/jquery-ui.min.css" type="text/css">
    <link rel="stylesheet" href="./Assignment Day1_files/jquery.typeahead.min.css" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    


<script type="text/javascript" src="./Assignment Day1_files/MathJax.js.download" charset="utf-8"></script>

<script type="text/javascript">
// MathJax disabled, set as null to distinguish from *missing* MathJax,
// where it will be undefined, and should prompt a dialog later.
window.mathjax_url = "/static/components/MathJax/MathJax.js";
</script>

<link rel="stylesheet" href="./Assignment Day1_files/bootstrap-tour.min.css" type="text/css">
<link rel="stylesheet" href="./Assignment Day1_files/codemirror.css">


    <link rel="stylesheet" href="./Assignment Day1_files/style.min.css" type="text/css">
    

<link rel="stylesheet" href="./Assignment Day1_files/override.css" type="text/css">
<link rel="stylesheet" href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3" id="kernel-css" type="text/css">


    <link rel="stylesheet" href="./Assignment Day1_files/custom.css" type="text/css">
    <script src="./Assignment Day1_files/promise.min.js.download" type="text/javascript" charset="utf-8"></script>
    <script src="./Assignment Day1_files/react.production.min.js.download" type="text/javascript"></script>
    <script src="./Assignment Day1_files/react-dom.production.min.js.download" type="text/javascript"></script>
    <script src="./Assignment Day1_files/index.js.download" type="text/javascript"></script>
    <script src="./Assignment Day1_files/require.js.download" type="text/javascript" charset="utf-8"></script>
    <script>
      require.config({
          
          urlArgs: "v=20210706175842",
          
          baseUrl: '/static/',
          paths: {
            'auth/js/main': 'auth/js/main.min',
            custom : '/custom',
            nbextensions : '/nbextensions',
            kernelspecs : '/kernelspecs',
            underscore : 'components/underscore/underscore-min',
            backbone : 'components/backbone/backbone-min',
            jed: 'components/jed/jed',
            jquery: 'components/jquery/jquery.min',
            json: 'components/requirejs-plugins/src/json',
            text: 'components/requirejs-text/text',
            bootstrap: 'components/bootstrap/dist/js/bootstrap.min',
            bootstraptour: 'components/bootstrap-tour/build/js/bootstrap-tour.min',
            'jquery-ui': 'components/jquery-ui/jquery-ui.min',
            moment: 'components/moment/min/moment-with-locales',
            codemirror: 'components/codemirror',
            termjs: 'components/xterm.js/xterm',
            typeahead: 'components/jquery-typeahead/dist/jquery.typeahead.min',
          },
          map: { // for backward compatibility
              "*": {
                  "jqueryui": "jquery-ui",
              }
          },
          shim: {
            typeahead: {
              deps: ["jquery"],
              exports: "typeahead"
            },
            underscore: {
              exports: '_'
            },
            backbone: {
              deps: ["underscore", "jquery"],
              exports: "Backbone"
            },
            bootstrap: {
              deps: ["jquery"],
              exports: "bootstrap"
            },
            bootstraptour: {
              deps: ["bootstrap"],
              exports: "Tour"
            },
            "jquery-ui": {
              deps: ["jquery"],
              exports: "$"
            }
          },
          waitSeconds: 30,
      });

      require.config({
          map: {
              '*':{
                'contents': 'services/contents',
              }
          }
      });

      // error-catching custom.js shim.
      define("custom", function (require, exports, module) {
          try {
              var custom = require('custom/custom');
              console.debug('loaded custom.js');
              return custom;
          } catch (e) {
              console.error("error loading custom.js", e);
              return {};
          }
      })

    document.nbjs_translations = {"domain": "nbjs", "locale_data": {"nbjs": {"": {"domain": "nbjs"}}}};
    document.documentElement.lang = navigator.language.toLowerCase();
    </script>

    
    

<script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="services/contents" src="./Assignment Day1_files/contents.js.download"></script><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MathJax_Preview .MJXf-math {color: inherit!important}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="custom/custom" src="./Assignment Day1_files/custom.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="nbextensions/jupyter-js-widgets/extension" src="./Assignment Day1_files/extension.js.download"></script><style type="text/css">div.MathJax_MathML {text-align: center; margin: .75em 0px; display: block!important}
.MathJax_MathML {font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
span.MathJax_MathML {display: inline!important}
.MathJax_mmlExBox {display: block!important; overflow: hidden; height: 1px; width: 60ex; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0}
[class="MJX-tex-oldstyle"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB}
[class="MJX-tex-oldstyle-bold"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB; font-weight: bold}
[class="MJX-tex-caligraphic"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB}
[class="MJX-tex-caligraphic-bold"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB; font-weight: bold}
@font-face /*1*/ {font-family: MathJax_Caligraphic-WEB; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf')}
@font-face /*2*/ {font-family: MathJax_Caligraphic-WEB; font-weight: bold; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Bold.otf')}
[mathvariant="double-struck"] {font-family: MathJax_AMS, MathJax_AMS-WEB}
[mathvariant="script"] {font-family: MathJax_Script, MathJax_Script-WEB}
[mathvariant="fraktur"] {font-family: MathJax_Fraktur, MathJax_Fraktur-WEB}
[mathvariant="bold-script"] {font-family: MathJax_Script, MathJax_Caligraphic-WEB; font-weight: bold}
[mathvariant="bold-fraktur"] {font-family: MathJax_Fraktur, MathJax_Fraktur-WEB; font-weight: bold}
[mathvariant="monospace"] {font-family: monospace}
[mathvariant="sans-serif"] {font-family: sans-serif}
[mathvariant="bold-sans-serif"] {font-family: sans-serif; font-weight: bold}
[mathvariant="sans-serif-italic"] {font-family: sans-serif; font-style: italic}
[mathvariant="sans-serif-bold-italic"] {font-family: sans-serif; font-style: italic; font-weight: bold}
@font-face /*3*/ {font-family: MathJax_AMS-WEB; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_AMS-Regular.otf')}
@font-face /*4*/ {font-family: MathJax_Script-WEB; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Script-Regular.otf')}
@font-face /*5*/ {font-family: MathJax_Fraktur-WEB; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Fraktur-Regular.otf')}
@font-face /*6*/ {font-family: MathJax_Fraktur-WEB; font-weight: bold; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Fraktur-Bold.otf')}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Blank; src: url('about:blank')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/* Override the correction for the prompt area in https://github.com/jupyter/notebook/blob/dd41d9fd5c4f698bd7468612d877828a7eeb0e7a/IPython/html/static/notebook/less/outputarea.less#L110 */
.jupyter-widgets-output-area div.output_subarea {
    max-width: 100%;
}

/* Work-around for the bug fixed in https://github.com/jupyter/notebook/pull/2961 */
.jupyter-widgets-output-area > .out_prompt_overlay {
    display: none;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-Widget {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  cursor: default;
}


.p-Widget.p-mod-hidden {
  display: none !important;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-CommandPalette {
  display: flex;
  flex-direction: column;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


.p-CommandPalette-search {
  flex: 0 0 auto;
}


.p-CommandPalette-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  min-height: 0;
  overflow: auto;
  list-style-type: none;
}


.p-CommandPalette-header {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}


.p-CommandPalette-item {
  display: flex;
  flex-direction: row;
}


.p-CommandPalette-itemIcon {
  flex: 0 0 auto;
}


.p-CommandPalette-itemContent {
  flex: 1 1 auto;
  overflow: hidden;
}


.p-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}


.p-CommandPalette-itemLabel {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-DockPanel {
  z-index: 0;
}


.p-DockPanel-widget {
  z-index: 0;
}


.p-DockPanel-tabBar {
  z-index: 1;
}


.p-DockPanel-handle {
  z-index: 2;
}


.p-DockPanel-handle.p-mod-hidden {
  display: none !important;
}


.p-DockPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}


.p-DockPanel-handle[data-orientation='horizontal'] {
  cursor: ew-resize;
}


.p-DockPanel-handle[data-orientation='vertical'] {
  cursor: ns-resize;
}


.p-DockPanel-handle[data-orientation='horizontal']:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}


.p-DockPanel-handle[data-orientation='vertical']:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}


.p-DockPanel-overlay {
  z-index: 3;
  box-sizing: border-box;
  pointer-events: none;
}


.p-DockPanel-overlay.p-mod-hidden {
  display: none !important;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-Menu {
  z-index: 10000;
  position: absolute;
  white-space: nowrap;
  overflow-x: hidden;
  overflow-y: auto;
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


.p-Menu-content {
  margin: 0;
  padding: 0;
  display: table;
  list-style-type: none;
}


.p-Menu-item {
  display: table-row;
}


.p-Menu-item.p-mod-hidden,
.p-Menu-item.p-mod-collapsed {
  display: none !important;
}


.p-Menu-itemIcon,
.p-Menu-itemSubmenuIcon {
  display: table-cell;
  text-align: center;
}


.p-Menu-itemLabel {
  display: table-cell;
  text-align: left;
}


.p-Menu-itemShortcut {
  display: table-cell;
  text-align: right;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-MenuBar {
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


.p-MenuBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: row;
  list-style-type: none;
}


.p-MenuBar-item {
  box-sizing: border-box;
}


.p-MenuBar-itemIcon,
.p-MenuBar-itemLabel {
  display: inline-block;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-ScrollBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


.p-ScrollBar[data-orientation='horizontal'] {
  flex-direction: row;
}


.p-ScrollBar[data-orientation='vertical'] {
  flex-direction: column;
}


.p-ScrollBar-button {
  box-sizing: border-box;
  flex: 0 0 auto;
}


.p-ScrollBar-track {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  flex: 1 1 auto;
}


.p-ScrollBar-thumb {
  box-sizing: border-box;
  position: absolute;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-SplitPanel-child {
  z-index: 0;
}


.p-SplitPanel-handle {
  z-index: 1;
}


.p-SplitPanel-handle.p-mod-hidden {
  display: none !important;
}


.p-SplitPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}


.p-SplitPanel[data-orientation='horizontal'] > .p-SplitPanel-handle {
  cursor: ew-resize;
}


.p-SplitPanel[data-orientation='vertical'] > .p-SplitPanel-handle {
  cursor: ns-resize;
}


.p-SplitPanel[data-orientation='horizontal'] > .p-SplitPanel-handle:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}


.p-SplitPanel[data-orientation='vertical'] > .p-SplitPanel-handle:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-TabBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


.p-TabBar[data-orientation='horizontal'] {
  flex-direction: row;
}


.p-TabBar[data-orientation='vertical'] {
  flex-direction: column;
}


.p-TabBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex: 1 1 auto;
  list-style-type: none;
}


.p-TabBar[data-orientation='horizontal'] > .p-TabBar-content {
  flex-direction: row;
}


.p-TabBar[data-orientation='vertical'] > .p-TabBar-content {
  flex-direction: column;
}


.p-TabBar-tab {
  display: flex;
  flex-direction: row;
  box-sizing: border-box;
  overflow: hidden;
}


.p-TabBar-tabIcon,
.p-TabBar-tabCloseIcon {
  flex: 0 0 auto;
}


.p-TabBar-tabLabel {
  flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}


.p-TabBar-tab.p-mod-hidden {
  display: none !important;
}


.p-TabBar.p-mod-dragging .p-TabBar-tab {
  position: relative;
}


.p-TabBar.p-mod-dragging[data-orientation='horizontal'] .p-TabBar-tab {
  left: 0;
  transition: left 150ms ease;
}


.p-TabBar.p-mod-dragging[data-orientation='vertical'] .p-TabBar-tab {
  top: 0;
  transition: top 150ms ease;
}


.p-TabBar.p-mod-dragging .p-TabBar-tab.p-mod-dragging {
  transition: none;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-TabPanel-tabBar {
  z-index: 1;
}


.p-TabPanel-stackedPanel {
  z-index: 0;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
</style><style type="text/css">/* Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

 .jupyter-widgets-disconnected::before {
    content: "\f127"; /* chain-broken */
    display: inline-block;
    font: normal normal normal 14px/1 FontAwesome;
    font-size: inherit;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #d9534f;
    padding: 3px;
    align-self: flex-start;
}
</style><style type="text/css">/**
 * The material design colors are adapted from google-material-color v1.2.6
 * https://github.com/danlevan/google-material-color
 * https://github.com/danlevan/google-material-color/blob/f67ca5f4028b2f1b34862f64b0ca67323f91b088/dist/palette.var.css
 *
 * The license for the material design color CSS variables is as follows (see
 * https://github.com/danlevan/google-material-color/blob/f67ca5f4028b2f1b34862f64b0ca67323f91b088/LICENSE)
 *
 * The MIT License (MIT)
 *
 * Copyright (c) 2014 Dan Le Van
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */
:root {
  --md-red-50: #FFEBEE;
  --md-red-100: #FFCDD2;
  --md-red-200: #EF9A9A;
  --md-red-300: #E57373;
  --md-red-400: #EF5350;
  --md-red-500: #F44336;
  --md-red-600: #E53935;
  --md-red-700: #D32F2F;
  --md-red-800: #C62828;
  --md-red-900: #B71C1C;
  --md-red-A100: #FF8A80;
  --md-red-A200: #FF5252;
  --md-red-A400: #FF1744;
  --md-red-A700: #D50000;

  --md-pink-50: #FCE4EC;
  --md-pink-100: #F8BBD0;
  --md-pink-200: #F48FB1;
  --md-pink-300: #F06292;
  --md-pink-400: #EC407A;
  --md-pink-500: #E91E63;
  --md-pink-600: #D81B60;
  --md-pink-700: #C2185B;
  --md-pink-800: #AD1457;
  --md-pink-900: #880E4F;
  --md-pink-A100: #FF80AB;
  --md-pink-A200: #FF4081;
  --md-pink-A400: #F50057;
  --md-pink-A700: #C51162;

  --md-purple-50: #F3E5F5;
  --md-purple-100: #E1BEE7;
  --md-purple-200: #CE93D8;
  --md-purple-300: #BA68C8;
  --md-purple-400: #AB47BC;
  --md-purple-500: #9C27B0;
  --md-purple-600: #8E24AA;
  --md-purple-700: #7B1FA2;
  --md-purple-800: #6A1B9A;
  --md-purple-900: #4A148C;
  --md-purple-A100: #EA80FC;
  --md-purple-A200: #E040FB;
  --md-purple-A400: #D500F9;
  --md-purple-A700: #AA00FF;

  --md-deep-purple-50: #EDE7F6;
  --md-deep-purple-100: #D1C4E9;
  --md-deep-purple-200: #B39DDB;
  --md-deep-purple-300: #9575CD;
  --md-deep-purple-400: #7E57C2;
  --md-deep-purple-500: #673AB7;
  --md-deep-purple-600: #5E35B1;
  --md-deep-purple-700: #512DA8;
  --md-deep-purple-800: #4527A0;
  --md-deep-purple-900: #311B92;
  --md-deep-purple-A100: #B388FF;
  --md-deep-purple-A200: #7C4DFF;
  --md-deep-purple-A400: #651FFF;
  --md-deep-purple-A700: #6200EA;

  --md-indigo-50: #E8EAF6;
  --md-indigo-100: #C5CAE9;
  --md-indigo-200: #9FA8DA;
  --md-indigo-300: #7986CB;
  --md-indigo-400: #5C6BC0;
  --md-indigo-500: #3F51B5;
  --md-indigo-600: #3949AB;
  --md-indigo-700: #303F9F;
  --md-indigo-800: #283593;
  --md-indigo-900: #1A237E;
  --md-indigo-A100: #8C9EFF;
  --md-indigo-A200: #536DFE;
  --md-indigo-A400: #3D5AFE;
  --md-indigo-A700: #304FFE;

  --md-blue-50: #E3F2FD;
  --md-blue-100: #BBDEFB;
  --md-blue-200: #90CAF9;
  --md-blue-300: #64B5F6;
  --md-blue-400: #42A5F5;
  --md-blue-500: #2196F3;
  --md-blue-600: #1E88E5;
  --md-blue-700: #1976D2;
  --md-blue-800: #1565C0;
  --md-blue-900: #0D47A1;
  --md-blue-A100: #82B1FF;
  --md-blue-A200: #448AFF;
  --md-blue-A400: #2979FF;
  --md-blue-A700: #2962FF;

  --md-light-blue-50: #E1F5FE;
  --md-light-blue-100: #B3E5FC;
  --md-light-blue-200: #81D4FA;
  --md-light-blue-300: #4FC3F7;
  --md-light-blue-400: #29B6F6;
  --md-light-blue-500: #03A9F4;
  --md-light-blue-600: #039BE5;
  --md-light-blue-700: #0288D1;
  --md-light-blue-800: #0277BD;
  --md-light-blue-900: #01579B;
  --md-light-blue-A100: #80D8FF;
  --md-light-blue-A200: #40C4FF;
  --md-light-blue-A400: #00B0FF;
  --md-light-blue-A700: #0091EA;

  --md-cyan-50: #E0F7FA;
  --md-cyan-100: #B2EBF2;
  --md-cyan-200: #80DEEA;
  --md-cyan-300: #4DD0E1;
  --md-cyan-400: #26C6DA;
  --md-cyan-500: #00BCD4;
  --md-cyan-600: #00ACC1;
  --md-cyan-700: #0097A7;
  --md-cyan-800: #00838F;
  --md-cyan-900: #006064;
  --md-cyan-A100: #84FFFF;
  --md-cyan-A200: #18FFFF;
  --md-cyan-A400: #00E5FF;
  --md-cyan-A700: #00B8D4;

  --md-teal-50: #E0F2F1;
  --md-teal-100: #B2DFDB;
  --md-teal-200: #80CBC4;
  --md-teal-300: #4DB6AC;
  --md-teal-400: #26A69A;
  --md-teal-500: #009688;
  --md-teal-600: #00897B;
  --md-teal-700: #00796B;
  --md-teal-800: #00695C;
  --md-teal-900: #004D40;
  --md-teal-A100: #A7FFEB;
  --md-teal-A200: #64FFDA;
  --md-teal-A400: #1DE9B6;
  --md-teal-A700: #00BFA5;

  --md-green-50: #E8F5E9;
  --md-green-100: #C8E6C9;
  --md-green-200: #A5D6A7;
  --md-green-300: #81C784;
  --md-green-400: #66BB6A;
  --md-green-500: #4CAF50;
  --md-green-600: #43A047;
  --md-green-700: #388E3C;
  --md-green-800: #2E7D32;
  --md-green-900: #1B5E20;
  --md-green-A100: #B9F6CA;
  --md-green-A200: #69F0AE;
  --md-green-A400: #00E676;
  --md-green-A700: #00C853;

  --md-light-green-50: #F1F8E9;
  --md-light-green-100: #DCEDC8;
  --md-light-green-200: #C5E1A5;
  --md-light-green-300: #AED581;
  --md-light-green-400: #9CCC65;
  --md-light-green-500: #8BC34A;
  --md-light-green-600: #7CB342;
  --md-light-green-700: #689F38;
  --md-light-green-800: #558B2F;
  --md-light-green-900: #33691E;
  --md-light-green-A100: #CCFF90;
  --md-light-green-A200: #B2FF59;
  --md-light-green-A400: #76FF03;
  --md-light-green-A700: #64DD17;

  --md-lime-50: #F9FBE7;
  --md-lime-100: #F0F4C3;
  --md-lime-200: #E6EE9C;
  --md-lime-300: #DCE775;
  --md-lime-400: #D4E157;
  --md-lime-500: #CDDC39;
  --md-lime-600: #C0CA33;
  --md-lime-700: #AFB42B;
  --md-lime-800: #9E9D24;
  --md-lime-900: #827717;
  --md-lime-A100: #F4FF81;
  --md-lime-A200: #EEFF41;
  --md-lime-A400: #C6FF00;
  --md-lime-A700: #AEEA00;

  --md-yellow-50: #FFFDE7;
  --md-yellow-100: #FFF9C4;
  --md-yellow-200: #FFF59D;
  --md-yellow-300: #FFF176;
  --md-yellow-400: #FFEE58;
  --md-yellow-500: #FFEB3B;
  --md-yellow-600: #FDD835;
  --md-yellow-700: #FBC02D;
  --md-yellow-800: #F9A825;
  --md-yellow-900: #F57F17;
  --md-yellow-A100: #FFFF8D;
  --md-yellow-A200: #FFFF00;
  --md-yellow-A400: #FFEA00;
  --md-yellow-A700: #FFD600;

  --md-amber-50: #FFF8E1;
  --md-amber-100: #FFECB3;
  --md-amber-200: #FFE082;
  --md-amber-300: #FFD54F;
  --md-amber-400: #FFCA28;
  --md-amber-500: #FFC107;
  --md-amber-600: #FFB300;
  --md-amber-700: #FFA000;
  --md-amber-800: #FF8F00;
  --md-amber-900: #FF6F00;
  --md-amber-A100: #FFE57F;
  --md-amber-A200: #FFD740;
  --md-amber-A400: #FFC400;
  --md-amber-A700: #FFAB00;

  --md-orange-50: #FFF3E0;
  --md-orange-100: #FFE0B2;
  --md-orange-200: #FFCC80;
  --md-orange-300: #FFB74D;
  --md-orange-400: #FFA726;
  --md-orange-500: #FF9800;
  --md-orange-600: #FB8C00;
  --md-orange-700: #F57C00;
  --md-orange-800: #EF6C00;
  --md-orange-900: #E65100;
  --md-orange-A100: #FFD180;
  --md-orange-A200: #FFAB40;
  --md-orange-A400: #FF9100;
  --md-orange-A700: #FF6D00;

  --md-deep-orange-50: #FBE9E7;
  --md-deep-orange-100: #FFCCBC;
  --md-deep-orange-200: #FFAB91;
  --md-deep-orange-300: #FF8A65;
  --md-deep-orange-400: #FF7043;
  --md-deep-orange-500: #FF5722;
  --md-deep-orange-600: #F4511E;
  --md-deep-orange-700: #E64A19;
  --md-deep-orange-800: #D84315;
  --md-deep-orange-900: #BF360C;
  --md-deep-orange-A100: #FF9E80;
  --md-deep-orange-A200: #FF6E40;
  --md-deep-orange-A400: #FF3D00;
  --md-deep-orange-A700: #DD2C00;

  --md-brown-50: #EFEBE9;
  --md-brown-100: #D7CCC8;
  --md-brown-200: #BCAAA4;
  --md-brown-300: #A1887F;
  --md-brown-400: #8D6E63;
  --md-brown-500: #795548;
  --md-brown-600: #6D4C41;
  --md-brown-700: #5D4037;
  --md-brown-800: #4E342E;
  --md-brown-900: #3E2723;

  --md-grey-50: #FAFAFA;
  --md-grey-100: #F5F5F5;
  --md-grey-200: #EEEEEE;
  --md-grey-300: #E0E0E0;
  --md-grey-400: #BDBDBD;
  --md-grey-500: #9E9E9E;
  --md-grey-600: #757575;
  --md-grey-700: #616161;
  --md-grey-800: #424242;
  --md-grey-900: #212121;

  --md-blue-grey-50: #ECEFF1;
  --md-blue-grey-100: #CFD8DC;
  --md-blue-grey-200: #B0BEC5;
  --md-blue-grey-300: #90A4AE;
  --md-blue-grey-400: #78909C;
  --md-blue-grey-500: #607D8B;
  --md-blue-grey-600: #546E7A;
  --md-blue-grey-700: #455A64;
  --md-blue-grey-800: #37474F;
  --md-blue-grey-900: #263238;
}</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
This file is copied from the JupyterLab project to define default styling for
when the widget styling is compiled down to eliminate CSS variables. We make one
change - we comment out the font import below.
*/

/*
The following CSS variables define the main, public API for styling JupyterLab.
These variables should be used by all plugins wherever possible. In other
words, plugins should not define custom colors, sizes, etc unless absolutely
necessary. This enables users to change the visual theme of JupyterLab
by changing these variables.

Many variables appear in an ordered sequence (0,1,2,3). These sequences
are designed to work well together, so for example, `--jp-border-color1` should
be used with `--jp-layout-color1`. The numbers have the following meanings:

* 0: super-primary, reserved for special emphasis
* 1: primary, most important under normal situations
* 2: secondary, next most important under normal situations
* 3: tertiary, next most important under normal situations

Throughout JupyterLab, we are mostly following principles from Google's
Material Design when selecting colors. We are not, however, following
all of MD as it is not optimized for dense, information rich UIs.
*/


/*
 * Optional monospace font for input/output prompt.
 */
 /* Commented out in ipywidgets since we don't need it. */
/* @import url('https://fonts.googleapis.com/css?family=Roboto+Mono'); */

/*
 * Added for compabitility with output area
 */
:root {
  --jp-icon-search: none;
  --jp-ui-select-caret: none;
}


:root {

  /* Borders

  The following variables, specify the visual styling of borders in JupyterLab.
   */

  --jp-border-width: 1px;
  --jp-border-color0: var(--md-grey-700);
  --jp-border-color1: var(--md-grey-500);
  --jp-border-color2: var(--md-grey-300);
  --jp-border-color3: var(--md-grey-100);

  /* UI Fonts

  The UI font CSS variables are used for the typography all of the JupyterLab
  user interface elements that are not directly user generated content.
  */

  --jp-ui-font-scale-factor: 1.2;
  --jp-ui-font-size0: calc(var(--jp-ui-font-size1)/var(--jp-ui-font-scale-factor));
  --jp-ui-font-size1: 13px; /* Base font size */
  --jp-ui-font-size2: calc(var(--jp-ui-font-size1)*var(--jp-ui-font-scale-factor));
  --jp-ui-font-size3: calc(var(--jp-ui-font-size2)*var(--jp-ui-font-scale-factor));
  --jp-ui-icon-font-size: 14px; /* Ensures px perfect FontAwesome icons */
  --jp-ui-font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;

  /* Use these font colors against the corresponding main layout colors.
     In a light theme, these go from dark to light.
  */

  --jp-ui-font-color0: rgba(0,0,0,1.0);
  --jp-ui-font-color1: rgba(0,0,0,0.8);
  --jp-ui-font-color2: rgba(0,0,0,0.5);
  --jp-ui-font-color3: rgba(0,0,0,0.3);

  /* Use these against the brand/accent/warn/error colors.
     These will typically go from light to darker, in both a dark and light theme
   */

  --jp-inverse-ui-font-color0: rgba(255,255,255,1);
  --jp-inverse-ui-font-color1: rgba(255,255,255,1.0);
  --jp-inverse-ui-font-color2: rgba(255,255,255,0.7);
  --jp-inverse-ui-font-color3: rgba(255,255,255,0.5);

  /* Content Fonts

  Content font variables are used for typography of user generated content.
  */

  --jp-content-font-size: 13px;
  --jp-content-line-height: 1.5;
  --jp-content-font-color0: black;
  --jp-content-font-color1: black;
  --jp-content-font-color2: var(--md-grey-700);
  --jp-content-font-color3: var(--md-grey-500);

  --jp-ui-font-scale-factor: 1.2;
  --jp-ui-font-size0: calc(var(--jp-ui-font-size1)/var(--jp-ui-font-scale-factor));
  --jp-ui-font-size1: 13px; /* Base font size */
  --jp-ui-font-size2: calc(var(--jp-ui-font-size1)*var(--jp-ui-font-scale-factor));
  --jp-ui-font-size3: calc(var(--jp-ui-font-size2)*var(--jp-ui-font-scale-factor));

  --jp-code-font-size: 13px;
  --jp-code-line-height: 1.307;
  --jp-code-padding: 5px;
  --jp-code-font-family: monospace;


  /* Layout

  The following are the main layout colors use in JupyterLab. In a light
  theme these would go from light to dark.
  */

  --jp-layout-color0: white;
  --jp-layout-color1: white;
  --jp-layout-color2: var(--md-grey-200);
  --jp-layout-color3: var(--md-grey-400);

  /* Brand/accent */

  --jp-brand-color0: var(--md-blue-700);
  --jp-brand-color1: var(--md-blue-500);
  --jp-brand-color2: var(--md-blue-300);
  --jp-brand-color3: var(--md-blue-100);

  --jp-accent-color0: var(--md-green-700);
  --jp-accent-color1: var(--md-green-500);
  --jp-accent-color2: var(--md-green-300);
  --jp-accent-color3: var(--md-green-100);

  /* State colors (warn, error, success, info) */

  --jp-warn-color0: var(--md-orange-700);
  --jp-warn-color1: var(--md-orange-500);
  --jp-warn-color2: var(--md-orange-300);
  --jp-warn-color3: var(--md-orange-100);

  --jp-error-color0: var(--md-red-700);
  --jp-error-color1: var(--md-red-500);
  --jp-error-color2: var(--md-red-300);
  --jp-error-color3: var(--md-red-100);

  --jp-success-color0: var(--md-green-700);
  --jp-success-color1: var(--md-green-500);
  --jp-success-color2: var(--md-green-300);
  --jp-success-color3: var(--md-green-100);

  --jp-info-color0: var(--md-cyan-700);
  --jp-info-color1: var(--md-cyan-500);
  --jp-info-color2: var(--md-cyan-300);
  --jp-info-color3: var(--md-cyan-100);

  /* Cell specific styles */

  --jp-cell-padding: 5px;
  --jp-cell-editor-background: #f7f7f7;
  --jp-cell-editor-border-color: #cfcfcf;
  --jp-cell-editor-background-edit: var(--jp-ui-layout-color1);
  --jp-cell-editor-border-color-edit: var(--jp-brand-color1);
  --jp-cell-prompt-width: 100px;
  --jp-cell-prompt-font-family: 'Roboto Mono', monospace;
  --jp-cell-prompt-letter-spacing: 0px;
  --jp-cell-prompt-opacity: 1.0;
  --jp-cell-prompt-opacity-not-active: 0.4;
  --jp-cell-prompt-font-color-not-active: var(--md-grey-700);
  /* A custom blend of MD grey and blue 600
   * See https://meyerweb.com/eric/tools/color-blend/#546E7A:1E88E5:5:hex */
  --jp-cell-inprompt-font-color: #307FC1;
  /* A custom blend of MD grey and orange 600
   * https://meyerweb.com/eric/tools/color-blend/#546E7A:F4511E:5:hex */
  --jp-cell-outprompt-font-color: #BF5B3D;

  /* Notebook specific styles */

  --jp-notebook-padding: 10px;
  --jp-notebook-scroll-padding: 100px;

  /* Console specific styles */

  --jp-console-background: var(--md-grey-100);

  /* Toolbar specific styles */

  --jp-toolbar-border-color: var(--md-grey-400);
  --jp-toolbar-micro-height: 8px;
  --jp-toolbar-background: var(--jp-layout-color0);
  --jp-toolbar-box-shadow: 0px 0px 2px 0px rgba(0,0,0,0.24);
  --jp-toolbar-header-margin: 4px 4px 0px 4px;
  --jp-toolbar-active-background: var(--md-grey-300);
}
</style><style type="text/css">/* This file has code derived from PhosphorJS CSS files, as noted below. The license for this PhosphorJS code is:

Copyright (c) 2014-2017, PhosphorJS Contributors
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

*/

/*
 * The following section is derived from https://github.com/phosphorjs/phosphor/blob/23b9d075ebc5b73ab148b6ebfc20af97f85714c4/packages/widgets/style/tabbar.css 
 * We've scoped the rules so that they are consistent with exactly our code.
 */

.jupyter-widgets.widget-tab > .p-TabBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


.jupyter-widgets.widget-tab > .p-TabBar[data-orientation='horizontal'] {
  flex-direction: row;
}


.jupyter-widgets.widget-tab > .p-TabBar[data-orientation='vertical'] {
  flex-direction: column;
}


.jupyter-widgets.widget-tab > .p-TabBar > .p-TabBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex: 1 1 auto;
  list-style-type: none;
}


.jupyter-widgets.widget-tab > .p-TabBar[data-orientation='horizontal'] > .p-TabBar-content {
  flex-direction: row;
}


.jupyter-widgets.widget-tab > .p-TabBar[data-orientation='vertical'] > .p-TabBar-content {
  flex-direction: column;
}


.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab {
  display: flex;
  flex-direction: row;
  box-sizing: border-box;
  overflow: hidden;
}


.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabIcon,
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabCloseIcon {
  flex: 0 0 auto;
}


.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabLabel {
  flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}


.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab.p-mod-hidden {
  display: none !important;
}


.jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging .p-TabBar-tab {
  position: relative;
}


.jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging[data-orientation='horizontal'] .p-TabBar-tab {
  left: 0;
  transition: left 150ms ease;
}


.jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging[data-orientation='vertical'] .p-TabBar-tab {
  top: 0;
  transition: top 150ms ease;
}


.jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging .p-TabBar-tab.p-mod-dragging {
  transition: none;
}

/* End tabbar.css */
</style><style type="text/css">/* Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*
 * We assume that the CSS variables in
 * https://github.com/jupyterlab/jupyterlab/blob/master/src/default-theme/variables.css
 * have been defined.
 */

:root {
    --jp-widgets-color: var(--jp-content-font-color1);
    --jp-widgets-label-color: var(--jp-widgets-color);
    --jp-widgets-readout-color: var(--jp-widgets-color);
    --jp-widgets-font-size: var(--jp-ui-font-size1);
    --jp-widgets-margin: 2px;
    --jp-widgets-inline-height: 28px;
    --jp-widgets-inline-width: 300px;
    --jp-widgets-inline-width-short: calc(var(--jp-widgets-inline-width) / 2 - var(--jp-widgets-margin));
    --jp-widgets-inline-width-tiny: calc(var(--jp-widgets-inline-width-short) / 2 - var(--jp-widgets-margin));
    --jp-widgets-inline-margin: 4px; /* margin between inline elements */
    --jp-widgets-inline-label-width: 80px;
    --jp-widgets-border-width: var(--jp-border-width);
    --jp-widgets-vertical-height: 200px;
    --jp-widgets-horizontal-tab-height: 24px;
    --jp-widgets-horizontal-tab-width: 144px;
    --jp-widgets-horizontal-tab-top-border: 2px;
    --jp-widgets-progress-thickness: 20px;
    --jp-widgets-container-padding: 15px;
    --jp-widgets-input-padding: 4px;
    --jp-widgets-radio-item-height-adjustment: 8px;
    --jp-widgets-radio-item-height: calc(var(--jp-widgets-inline-height) - var(--jp-widgets-radio-item-height-adjustment));
    --jp-widgets-slider-track-thickness: 4px;
    --jp-widgets-slider-border-width: var(--jp-widgets-border-width);
    --jp-widgets-slider-handle-size: 16px;
    --jp-widgets-slider-handle-border-color: var(--jp-border-color1);
    --jp-widgets-slider-handle-background-color: var(--jp-layout-color1);
    --jp-widgets-slider-active-handle-color: var(--jp-brand-color1);
    --jp-widgets-menu-item-height: 24px;
    --jp-widgets-dropdown-arrow: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDE5LjIuMSwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPgo8c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IgoJIHZpZXdCb3g9IjAgMCAxOCAxOCIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgMTggMTg7IiB4bWw6c3BhY2U9InByZXNlcnZlIj4KPHN0eWxlIHR5cGU9InRleHQvY3NzIj4KCS5zdDB7ZmlsbDpub25lO30KPC9zdHlsZT4KPHBhdGggZD0iTTUuMiw1LjlMOSw5LjdsMy44LTMuOGwxLjIsMS4ybC00LjksNWwtNC45LTVMNS4yLDUuOXoiLz4KPHBhdGggY2xhc3M9InN0MCIgZD0iTTAtMC42aDE4djE4SDBWLTAuNnoiLz4KPC9zdmc+Cg");
    --jp-widgets-input-color: var(--jp-ui-font-color1);
    --jp-widgets-input-background-color: var(--jp-layout-color1);
    --jp-widgets-input-border-color: var(--jp-border-color1);
    --jp-widgets-input-focus-border-color: var(--jp-brand-color2);
    --jp-widgets-input-border-width: var(--jp-widgets-border-width);
    --jp-widgets-disabled-opacity: 0.6;

    /* From Material Design Lite */
    --md-shadow-key-umbra-opacity: 0.2;
    --md-shadow-key-penumbra-opacity: 0.14;
    --md-shadow-ambient-shadow-opacity: 0.12;
}

.jupyter-widgets {
    margin: var(--jp-widgets-margin);
    box-sizing: border-box;
    color: var(--jp-widgets-color);
    overflow: visible;
}

.jupyter-widgets.jupyter-widgets-disconnected::before {
    line-height: var(--jp-widgets-inline-height);
    height: var(--jp-widgets-inline-height);
}

.jp-Output-result > .jupyter-widgets {
    margin-left: 0;
    margin-right: 0;
}

/* vbox and hbox */

.widget-inline-hbox {
    /* Horizontal widgets */
    box-sizing: border-box;
    display: flex;
    flex-direction: row;
    align-items: baseline;
}

.widget-inline-vbox {
    /* Vertical Widgets */
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.widget-box {
    box-sizing: border-box;
    display: flex;
    margin: 0;
    overflow: auto;
}

.widget-gridbox {
    box-sizing: border-box;
    display: grid;
    margin: 0;
    overflow: auto;
}

.widget-hbox {
    flex-direction: row;
}

.widget-vbox {
    flex-direction: column;
}

/* General Button Styling */

.jupyter-button {
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 0px;
    padding-bottom: 0px;
    display: inline-block;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    text-align: center;
    font-size: var(--jp-widgets-font-size);
    cursor: pointer;

    height: var(--jp-widgets-inline-height);
    border: 0px solid;
    line-height: var(--jp-widgets-inline-height);
    box-shadow: none;

    color: var(--jp-ui-font-color1);
    background-color: var(--jp-layout-color2);
    border-color: var(--jp-border-color2);
    border: none;
    user-select: none;
}

.jupyter-button i.fa {
    margin-right: var(--jp-widgets-inline-margin);
    pointer-events: none;
}

.jupyter-button:empty:before {
    content: "\200b"; /* zero-width space */
}

.jupyter-widgets.jupyter-button:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

.jupyter-button i.fa.center {
    margin-right: 0;
}

.jupyter-button:hover:enabled, .jupyter-button:focus:enabled {
    /* MD Lite 2dp shadow */
    box-shadow: 0 2px 2px 0 rgba(0, 0, 0, var(--md-shadow-key-penumbra-opacity)),
                0 3px 1px -2px rgba(0, 0, 0, var(--md-shadow-key-umbra-opacity)),
                0 1px 5px 0 rgba(0, 0, 0, var(--md-shadow-ambient-shadow-opacity));
}

.jupyter-button:active, .jupyter-button.mod-active {
    /* MD Lite 4dp shadow */
    box-shadow: 0 4px 5px 0 rgba(0, 0, 0, var(--md-shadow-key-penumbra-opacity)),
                0 1px 10px 0 rgba(0, 0, 0, var(--md-shadow-ambient-shadow-opacity)),
                0 2px 4px -1px rgba(0, 0, 0, var(--md-shadow-key-umbra-opacity));
    color: var(--jp-ui-font-color1);
    background-color: var(--jp-layout-color3);
}

.jupyter-button:focus:enabled {
    outline: 1px solid var(--jp-widgets-input-focus-border-color);
}

/* Button "Primary" Styling */

.jupyter-button.mod-primary {
    color: var(--jp-inverse-ui-font-color1);
    background-color: var(--jp-brand-color1);
}

.jupyter-button.mod-primary.mod-active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-brand-color0);
}

.jupyter-button.mod-primary:active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-brand-color0);
}

/* Button "Success" Styling */

.jupyter-button.mod-success {
    color: var(--jp-inverse-ui-font-color1);
    background-color: var(--jp-success-color1);
}

.jupyter-button.mod-success.mod-active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-success-color0);
 }

.jupyter-button.mod-success:active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-success-color0);
 }

 /* Button "Info" Styling */

.jupyter-button.mod-info {
    color: var(--jp-inverse-ui-font-color1);
    background-color: var(--jp-info-color1);
}

.jupyter-button.mod-info.mod-active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-info-color0);
}

.jupyter-button.mod-info:active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-info-color0);
}

/* Button "Warning" Styling */

.jupyter-button.mod-warning {
    color: var(--jp-inverse-ui-font-color1);
    background-color: var(--jp-warn-color1);
}

.jupyter-button.mod-warning.mod-active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-warn-color0);
}

.jupyter-button.mod-warning:active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-warn-color0);
}

/* Button "Danger" Styling */

.jupyter-button.mod-danger {
    color: var(--jp-inverse-ui-font-color1);
    background-color: var(--jp-error-color1);
}

.jupyter-button.mod-danger.mod-active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-error-color0);
}

.jupyter-button.mod-danger:active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-error-color0);
}

/* Widget Button, Widget Toggle Button, Widget Upload */

.widget-button, .widget-toggle-button, .widget-upload {
    width: var(--jp-widgets-inline-width-short);
}

/* Widget Label Styling */

/* Override Bootstrap label css */
.jupyter-widgets label {
    margin-bottom: initial;
}

.widget-label-basic {
    /* Basic Label */
    color: var(--jp-widgets-label-color);
    font-size: var(--jp-widgets-font-size);
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    line-height: var(--jp-widgets-inline-height);
}

.widget-label {
    /* Label */
    color: var(--jp-widgets-label-color);
    font-size: var(--jp-widgets-font-size);
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    line-height: var(--jp-widgets-inline-height);
}

.widget-inline-hbox .widget-label {
    /* Horizontal Widget Label */
    color: var(--jp-widgets-label-color);
    text-align: right;
    margin-right: calc( var(--jp-widgets-inline-margin) * 2 );
    width: var(--jp-widgets-inline-label-width);
    flex-shrink: 0;
}

.widget-inline-vbox .widget-label {
    /* Vertical Widget Label */
    color: var(--jp-widgets-label-color);
    text-align: center;
    line-height: var(--jp-widgets-inline-height);
}

/* Widget Readout Styling */

.widget-readout {
    color: var(--jp-widgets-readout-color);
    font-size: var(--jp-widgets-font-size);
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
    overflow: hidden;
    white-space: nowrap;
    text-align: center;
}

.widget-readout.overflow {
    /* Overflowing Readout */

    /* From Material Design Lite
        shadow-key-umbra-opacity: 0.2;
        shadow-key-penumbra-opacity: 0.14;
        shadow-ambient-shadow-opacity: 0.12;
     */
    -webkit-box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.2),
                        0 3px 1px -2px rgba(0, 0, 0, 0.14),
                        0 1px 5px 0 rgba(0, 0, 0, 0.12);

    -moz-box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.2),
                     0 3px 1px -2px rgba(0, 0, 0, 0.14),
                     0 1px 5px 0 rgba(0, 0, 0, 0.12);

    box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.2),
                0 3px 1px -2px rgba(0, 0, 0, 0.14),
                0 1px 5px 0 rgba(0, 0, 0, 0.12);
}

.widget-inline-hbox .widget-readout {
    /* Horizontal Readout */
    text-align: center;
    max-width: var(--jp-widgets-inline-width-short);
    min-width: var(--jp-widgets-inline-width-tiny);
    margin-left: var(--jp-widgets-inline-margin);
}

.widget-inline-vbox .widget-readout {
    /* Vertical Readout */
    margin-top: var(--jp-widgets-inline-margin);
    /* as wide as the widget */
    width: inherit;
}

/* Widget Checkbox Styling */

.widget-checkbox {
    width: var(--jp-widgets-inline-width);
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
}

.widget-checkbox input[type="checkbox"] {
    margin: 0px calc( var(--jp-widgets-inline-margin) * 2 ) 0px 0px;
    line-height: var(--jp-widgets-inline-height);
    font-size: large;
    flex-grow: 1;
    flex-shrink: 0;
    align-self: center;
}

/* Widget Valid Styling */

.widget-valid {
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
    width: var(--jp-widgets-inline-width-short);
    font-size: var(--jp-widgets-font-size);
}

.widget-valid i:before {
    line-height: var(--jp-widgets-inline-height);
    margin-right: var(--jp-widgets-inline-margin);
    margin-left: var(--jp-widgets-inline-margin);

    /* from the fa class in FontAwesome: https://github.com/FortAwesome/Font-Awesome/blob/49100c7c3a7b58d50baa71efef11af41a66b03d3/css/font-awesome.css#L14 */
    display: inline-block;
    font: normal normal normal 14px/1 FontAwesome;
    font-size: inherit;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

.widget-valid.mod-valid i:before {
    content: "\f00c";
    color: green;
}

.widget-valid.mod-invalid i:before {
    content: "\f00d";
    color: red;
}

.widget-valid.mod-valid .widget-valid-readout {
    display: none;
}

/* Widget Text and TextArea Stying */

.widget-textarea, .widget-text {
    width: var(--jp-widgets-inline-width);
}

.widget-text input[type="text"], .widget-text input[type="number"]{
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
}

.widget-text input[type="text"]:disabled, .widget-text input[type="number"]:disabled, .widget-textarea textarea:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

.widget-text input[type="text"], .widget-text input[type="number"], .widget-textarea textarea {
    box-sizing: border-box;
    border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    background-color: var(--jp-widgets-input-background-color);
    color: var(--jp-widgets-input-color);
    font-size: var(--jp-widgets-font-size);
    flex-grow: 1;
    min-width: 0; /* This makes it possible for the flexbox to shrink this input */
    flex-shrink: 1;
    outline: none !important;
}
    
.widget-text input[type="text"], .widget-textarea textarea {
    padding: var(--jp-widgets-input-padding) calc( var(--jp-widgets-input-padding) *  2);
}

.widget-text input[type="number"] {
    padding: var(--jp-widgets-input-padding) 0 var(--jp-widgets-input-padding) calc(var(--jp-widgets-input-padding) *  2);
}

.widget-textarea textarea {
    height: inherit;
    width: inherit;
}

.widget-text input:focus, .widget-textarea textarea:focus {
    border-color: var(--jp-widgets-input-focus-border-color);
}

/* Widget Slider */

.widget-slider .ui-slider {
    /* Slider Track */
    border: var(--jp-widgets-slider-border-width) solid var(--jp-layout-color3);
    background: var(--jp-layout-color3);
    box-sizing: border-box;
    position: relative;
    border-radius: 0px;
}

.widget-slider .ui-slider .ui-slider-handle {
    /* Slider Handle */
    outline: none !important; /* focused slider handles are colored - see below */
    position: absolute;
    background-color: var(--jp-widgets-slider-handle-background-color);
    border: var(--jp-widgets-slider-border-width) solid var(--jp-widgets-slider-handle-border-color);
    box-sizing: border-box;
    z-index: 1;
    background-image: none; /* Override jquery-ui */
}

/* Override jquery-ui */
.widget-slider .ui-slider .ui-slider-handle:hover, .widget-slider .ui-slider .ui-slider-handle:focus {
    background-color: var(--jp-widgets-slider-active-handle-color);
    border: var(--jp-widgets-slider-border-width) solid var(--jp-widgets-slider-active-handle-color);
}

.widget-slider .ui-slider .ui-slider-handle:active {
    background-color: var(--jp-widgets-slider-active-handle-color);
    border-color: var(--jp-widgets-slider-active-handle-color);
    z-index: 2;
    transform: scale(1.2);
}

.widget-slider  .ui-slider .ui-slider-range {
    /* Interval between the two specified value of a double slider */
    position: absolute;
    background: var(--jp-widgets-slider-active-handle-color);
    z-index: 0;
}

/* Shapes of Slider Handles */

.widget-hslider .ui-slider .ui-slider-handle {
    width: var(--jp-widgets-slider-handle-size);
    height: var(--jp-widgets-slider-handle-size);
    margin-top: calc((var(--jp-widgets-slider-track-thickness) - var(--jp-widgets-slider-handle-size)) / 2 - var(--jp-widgets-slider-border-width));
    margin-left: calc(var(--jp-widgets-slider-handle-size) / -2 + var(--jp-widgets-slider-border-width));
    border-radius: 50%;
    top: 0;
}

.widget-vslider .ui-slider .ui-slider-handle {
    width: var(--jp-widgets-slider-handle-size);
    height: var(--jp-widgets-slider-handle-size);
    margin-bottom: calc(var(--jp-widgets-slider-handle-size) / -2 + var(--jp-widgets-slider-border-width));
    margin-left: calc((var(--jp-widgets-slider-track-thickness) - var(--jp-widgets-slider-handle-size)) / 2 - var(--jp-widgets-slider-border-width));
    border-radius: 50%;
    left: 0;
}

.widget-hslider .ui-slider .ui-slider-range {
    height: calc( var(--jp-widgets-slider-track-thickness) * 2 );
    margin-top: calc((var(--jp-widgets-slider-track-thickness) - var(--jp-widgets-slider-track-thickness) * 2 ) / 2 - var(--jp-widgets-slider-border-width));
}

.widget-vslider .ui-slider .ui-slider-range {
    width: calc( var(--jp-widgets-slider-track-thickness) * 2 );
    margin-left: calc((var(--jp-widgets-slider-track-thickness) - var(--jp-widgets-slider-track-thickness) * 2 ) / 2 - var(--jp-widgets-slider-border-width));
}

/* Horizontal Slider */

.widget-hslider {
    width: var(--jp-widgets-inline-width);
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);

    /* Override the align-items baseline. This way, the description and readout
    still seem to align their baseline properly, and we don't have to have
    align-self: stretch in the .slider-container. */
    align-items: center;
}

.widgets-slider .slider-container {
    overflow: visible;
}

.widget-hslider .slider-container {
    height: var(--jp-widgets-inline-height);
    margin-left: calc(var(--jp-widgets-slider-handle-size) / 2 - 2 * var(--jp-widgets-slider-border-width));
    margin-right: calc(var(--jp-widgets-slider-handle-size) / 2 - 2 * var(--jp-widgets-slider-border-width));
    flex: 1 1 var(--jp-widgets-inline-width-short);
}

.widget-hslider .ui-slider {
    /* Inner, invisible slide div */
    height: var(--jp-widgets-slider-track-thickness);
    margin-top: calc((var(--jp-widgets-inline-height) - var(--jp-widgets-slider-track-thickness)) / 2);
    width: 100%;
}

/* Vertical Slider */

.widget-vbox .widget-label {
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
}

.widget-vslider {
    /* Vertical Slider */
    height: var(--jp-widgets-vertical-height);
    width: var(--jp-widgets-inline-width-tiny);
}

.widget-vslider .slider-container {
    flex: 1 1 var(--jp-widgets-inline-width-short);
    margin-left: auto;
    margin-right: auto;
    margin-bottom: calc(var(--jp-widgets-slider-handle-size) / 2 - 2 * var(--jp-widgets-slider-border-width));
    margin-top: calc(var(--jp-widgets-slider-handle-size) / 2 - 2 * var(--jp-widgets-slider-border-width));
    display: flex;
    flex-direction: column;
}

.widget-vslider .ui-slider-vertical {
    /* Inner, invisible slide div */
    width: var(--jp-widgets-slider-track-thickness);
    flex-grow: 1;
    margin-left: auto;
    margin-right: auto;
}

/* Widget Progress Styling */

.progress-bar {
    -webkit-transition: none;
    -moz-transition: none;
    -ms-transition: none;
    -o-transition: none;
    transition: none;
}

.progress-bar {
    height: var(--jp-widgets-inline-height);
}

.progress-bar {
    background-color: var(--jp-brand-color1);
}

.progress-bar-success {
    background-color: var(--jp-success-color1);
}

.progress-bar-info {
    background-color: var(--jp-info-color1);
}

.progress-bar-warning {
    background-color: var(--jp-warn-color1);
}

.progress-bar-danger {
    background-color: var(--jp-error-color1);
}

.progress {
    background-color: var(--jp-layout-color2);
    border: none;
    box-shadow: none;
}

/* Horisontal Progress */

.widget-hprogress {
    /* Progress Bar */
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
    width: var(--jp-widgets-inline-width);
    align-items: center;

}

.widget-hprogress .progress {
    flex-grow: 1;
    margin-top: var(--jp-widgets-input-padding);
    margin-bottom: var(--jp-widgets-input-padding);
    align-self: stretch;
    /* Override bootstrap style */
    height: initial;
}

/* Vertical Progress */

.widget-vprogress {
    height: var(--jp-widgets-vertical-height);
    width: var(--jp-widgets-inline-width-tiny);
}

.widget-vprogress .progress {
    flex-grow: 1;
    width: var(--jp-widgets-progress-thickness);
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 0;
}

/* Select Widget Styling */

.widget-dropdown {
    height: var(--jp-widgets-inline-height);
    width: var(--jp-widgets-inline-width);
    line-height: var(--jp-widgets-inline-height);
}

.widget-dropdown > select {
    padding-right: 20px;
    border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    border-radius: 0;
    height: inherit;
    flex: 1 1 var(--jp-widgets-inline-width-short);
    min-width: 0; /* This makes it possible for the flexbox to shrink this input */
    box-sizing: border-box;
    outline: none !important;
    box-shadow: none;
    background-color: var(--jp-widgets-input-background-color);
    color: var(--jp-widgets-input-color);
    font-size: var(--jp-widgets-font-size);
    vertical-align: top;
    padding-left: calc( var(--jp-widgets-input-padding) * 2);
	appearance: none;
	-webkit-appearance: none;
	-moz-appearance: none;
    background-repeat: no-repeat;
	background-size: 20px;
	background-position: right center;
    background-image: var(--jp-widgets-dropdown-arrow);
}
.widget-dropdown > select:focus {
    border-color: var(--jp-widgets-input-focus-border-color);
}

.widget-dropdown > select:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

/* To disable the dotted border in Firefox around select controls.
   See http://stackoverflow.com/a/18853002 */
.widget-dropdown > select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 #000;
}

/* Select and SelectMultiple */

.widget-select {
    width: var(--jp-widgets-inline-width);
    line-height: var(--jp-widgets-inline-height);

    /* Because Firefox defines the baseline of a select as the bottom of the
    control, we align the entire control to the top and add padding to the
    select to get an approximate first line baseline alignment. */
    align-items: flex-start;
}

.widget-select > select {
    border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    background-color: var(--jp-widgets-input-background-color);
    color: var(--jp-widgets-input-color);
    font-size: var(--jp-widgets-font-size);
    flex: 1 1 var(--jp-widgets-inline-width-short);
    outline: none !important;
    overflow: auto;
    height: inherit;

    /* Because Firefox defines the baseline of a select as the bottom of the
    control, we align the entire control to the top and add padding to the
    select to get an approximate first line baseline alignment. */
    padding-top: 5px;
}

.widget-select > select:focus {
    border-color: var(--jp-widgets-input-focus-border-color);
}

.wiget-select > select > option {
    padding-left: var(--jp-widgets-input-padding);
    line-height: var(--jp-widgets-inline-height);
    /* line-height doesn't work on some browsers for select options */
    padding-top: calc(var(--jp-widgets-inline-height)-var(--jp-widgets-font-size)/2);
    padding-bottom: calc(var(--jp-widgets-inline-height)-var(--jp-widgets-font-size)/2);
}



/* Toggle Buttons Styling */

.widget-toggle-buttons {
    line-height: var(--jp-widgets-inline-height);
}

.widget-toggle-buttons .widget-toggle-button {
    margin-left: var(--jp-widgets-margin);
    margin-right: var(--jp-widgets-margin);
}

.widget-toggle-buttons .jupyter-button:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

/* Radio Buttons Styling */

.widget-radio {
    width: var(--jp-widgets-inline-width);
    line-height: var(--jp-widgets-inline-height);
}

.widget-radio-box {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    box-sizing: border-box;
    flex-grow: 1;
    margin-bottom: var(--jp-widgets-radio-item-height-adjustment);
}

.widget-radio-box label {
    height: var(--jp-widgets-radio-item-height);
    line-height: var(--jp-widgets-radio-item-height);
    font-size: var(--jp-widgets-font-size);
}

.widget-radio-box input {
    height: var(--jp-widgets-radio-item-height);
    line-height: var(--jp-widgets-radio-item-height);
    margin: 0 calc( var(--jp-widgets-input-padding) * 2 ) 0 1px;
    float: left;
}

/* Color Picker Styling */

.widget-colorpicker {
    width: var(--jp-widgets-inline-width);
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
}

.widget-colorpicker > .widget-colorpicker-input {
    flex-grow: 1;
    flex-shrink: 1;
    min-width: var(--jp-widgets-inline-width-tiny);
}

.widget-colorpicker input[type="color"] {
    width: var(--jp-widgets-inline-height);
    height: var(--jp-widgets-inline-height);
    padding: 0 2px; /* make the color square actually square on Chrome on OS X */
    background: var(--jp-widgets-input-background-color);
    color: var(--jp-widgets-input-color);
    border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    border-left: none;
    flex-grow: 0;
    flex-shrink: 0;
    box-sizing: border-box;
    align-self: stretch;
    outline: none !important;
}

.widget-colorpicker.concise input[type="color"] {
    border-left: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
}

.widget-colorpicker input[type="color"]:focus, .widget-colorpicker input[type="text"]:focus {
    border-color: var(--jp-widgets-input-focus-border-color);
}

.widget-colorpicker input[type="text"] {
    flex-grow: 1;
    outline: none !important;
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
    background: var(--jp-widgets-input-background-color);
    color: var(--jp-widgets-input-color);
    border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    font-size: var(--jp-widgets-font-size);
    padding: var(--jp-widgets-input-padding) calc( var(--jp-widgets-input-padding) *  2 );
    min-width: 0; /* This makes it possible for the flexbox to shrink this input */
    flex-shrink: 1;
    box-sizing: border-box;
}

.widget-colorpicker input[type="text"]:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

/* Date Picker Styling */

.widget-datepicker {
    width: var(--jp-widgets-inline-width);
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
}

.widget-datepicker input[type="date"] {
    flex-grow: 1;
    flex-shrink: 1;
    min-width: 0; /* This makes it possible for the flexbox to shrink this input */
    outline: none !important;
    height: var(--jp-widgets-inline-height);
    border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    background-color: var(--jp-widgets-input-background-color);
    color: var(--jp-widgets-input-color);
    font-size: var(--jp-widgets-font-size);
    padding: var(--jp-widgets-input-padding) calc( var(--jp-widgets-input-padding) *  2 );
    box-sizing: border-box;
}

.widget-datepicker input[type="date"]:focus {
    border-color: var(--jp-widgets-input-focus-border-color);
}

.widget-datepicker input[type="date"]:invalid {
    border-color: var(--jp-warn-color1);
}

.widget-datepicker input[type="date"]:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

/* Play Widget */

.widget-play {
    width: var(--jp-widgets-inline-width-short);
    display: flex;
    align-items: stretch;
}

.widget-play .jupyter-button {
    flex-grow: 1;
    height: auto;
}

.widget-play .jupyter-button:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

/* Tab Widget */

.jupyter-widgets.widget-tab {
    display: flex;
    flex-direction: column;
}

.jupyter-widgets.widget-tab > .p-TabBar {
    /* Necessary so that a tab can be shifted down to overlay the border of the box below. */
    overflow-x: visible;
    overflow-y: visible;
}

.jupyter-widgets.widget-tab > .p-TabBar > .p-TabBar-content {
    /* Make sure that the tab grows from bottom up */
    align-items: flex-end;
    min-width: 0;
    min-height: 0;
}

.jupyter-widgets.widget-tab > .widget-tab-contents {
    width: 100%;
    box-sizing: border-box;
    margin: 0;
    background: var(--jp-layout-color1);
    color: var(--jp-ui-font-color1);
    border: var(--jp-border-width) solid var(--jp-border-color1);
    padding: var(--jp-widgets-container-padding);
    flex-grow: 1;
    overflow: auto;
}

.jupyter-widgets.widget-tab > .p-TabBar {
    font: var(--jp-widgets-font-size) Helvetica, Arial, sans-serif;
    min-height: calc(var(--jp-widgets-horizontal-tab-height) + var(--jp-border-width));
}

.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab {
    flex: 0 1 var(--jp-widgets-horizontal-tab-width);
    min-width: 35px;
    min-height: calc(var(--jp-widgets-horizontal-tab-height) + var(--jp-border-width));
    line-height: var(--jp-widgets-horizontal-tab-height);
    margin-left: calc(-1 * var(--jp-border-width));
    padding: 0px 10px;
    background: var(--jp-layout-color2);
    color: var(--jp-ui-font-color2);
    border: var(--jp-border-width) solid var(--jp-border-color1);
    border-bottom: none;
    position: relative;
}

.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab.p-mod-current {
    color: var(--jp-ui-font-color0);
    /* We want the background to match the tab content background */
    background: var(--jp-layout-color1);
    min-height: calc(var(--jp-widgets-horizontal-tab-height) + 2 * var(--jp-border-width));
    transform: translateY(var(--jp-border-width));
    overflow: visible;
}

.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab.p-mod-current:before {
    position: absolute;
    top: calc(-1 * var(--jp-border-width));
    left: calc(-1 * var(--jp-border-width));
    content: '';
    height: var(--jp-widgets-horizontal-tab-top-border);
    width: calc(100% + 2 * var(--jp-border-width));
    background: var(--jp-brand-color1);
}

.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab:first-child {
    margin-left: 0;
}

.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab:hover:not(.p-mod-current) {
    background: var(--jp-layout-color1);
    color: var(--jp-ui-font-color1);
}

.jupyter-widgets.widget-tab > .p-TabBar .p-mod-closable > .p-TabBar-tabCloseIcon {
    margin-left: 4px;
}

.jupyter-widgets.widget-tab > .p-TabBar .p-mod-closable > .p-TabBar-tabCloseIcon:before {
    font-family: FontAwesome;
    content: '\f00d'; /* close */
}

.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabIcon,
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabLabel,
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabCloseIcon {
    line-height: var(--jp-widgets-horizontal-tab-height);
}

/* Accordion Widget */

.p-Collapse {
    display: flex;
    flex-direction: column;
    align-items: stretch;
}

.p-Collapse-header {
    padding: var(--jp-widgets-input-padding);
    cursor: pointer;
    color: var(--jp-ui-font-color2);
    background-color: var(--jp-layout-color2);
    border: var(--jp-widgets-border-width) solid var(--jp-border-color1);
    padding: calc(var(--jp-widgets-container-padding) * 2 / 3) var(--jp-widgets-container-padding);
    font-weight: bold;
}

.p-Collapse-header:hover {
    background-color: var(--jp-layout-color1);
    color: var(--jp-ui-font-color1);
}

.p-Collapse-open > .p-Collapse-header {
    background-color: var(--jp-layout-color1);
    color: var(--jp-ui-font-color0);
    cursor: default;
    border-bottom: none;
}

.p-Collapse .p-Collapse-header::before {
    content: '\f0da\00A0';  /* caret-right, non-breaking space */
    display: inline-block;
    font: normal normal normal 14px/1 FontAwesome;
    font-size: inherit;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

.p-Collapse-open > .p-Collapse-header::before {
    content: '\f0d7\00A0'; /* caret-down, non-breaking space */
}

.p-Collapse-contents {
    padding: var(--jp-widgets-container-padding);
    background-color: var(--jp-layout-color1);
    color: var(--jp-ui-font-color1);
    border-left: var(--jp-widgets-border-width) solid var(--jp-border-color1);
    border-right: var(--jp-widgets-border-width) solid var(--jp-border-color1);
    border-bottom: var(--jp-widgets-border-width) solid var(--jp-border-color1);
    overflow: auto;
}

.p-Accordion {
    display: flex;
    flex-direction: column;
    align-items: stretch;
}

.p-Accordion .p-Collapse {
    margin-bottom: 0;
}

.p-Accordion .p-Collapse + .p-Collapse {
    margin-top: 4px;
}



/* HTML widget */

.widget-html, .widget-htmlmath {
    font-size: var(--jp-widgets-font-size);
}

.widget-html > .widget-html-content, .widget-htmlmath > .widget-html-content {
    /* Fill out the area in the HTML widget */
    align-self: stretch;
    flex-grow: 1;
    flex-shrink: 1;
    /* Makes sure the baseline is still aligned with other elements */
    line-height: var(--jp-widgets-inline-height);
    /* Make it possible to have absolutely-positioned elements in the html */
    position: relative;
}


/* Image widget  */

.widget-image {
    max-width: 100%;
    height: auto;
}
</style><style type="text/css">/* Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */
</style><link id="favicon" type="image/x-icon" rel="shortcut icon" href="http://localhost:8888/static/base/images/favicon-notebook.ico"></head>

<body class="notebook_app command_mode" data-jupyter-api-token="c01eb5d07063df624b1dbd9624d251aeee2982e42695de8e" data-base-url="/" data-ws-url="" data-notebook-name="Untitled.ipynb" data-notebook-path="Untitled.ipynb" dir="ltr"><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;"></div>

<noscript>
    <div id='noscript'>
      Jupyter Notebook requires JavaScript.<br>
      Please enable it to proceed. 
  </div>
</noscript>

<div id="header" role="navigation" aria-label="Top Menu" style="display: block;">
  <div id="header-container" class="container">
  <div id="ipython_notebook" class="nav navbar-brand"><a href="http://localhost:8888/tree?token=c01eb5d07063df624b1dbd9624d251aeee2982e42695de8e" title="dashboard">
      <img src="./Assignment Day1_files/logo.png" alt="Jupyter Notebook">
  </a></div>

  


<span id="save_widget" class="save_widget">
    <span id="notebook_name" class="filename">Untitled</span>
    <span class="checkpoint_status" title="Tue, Jul 6, 2021 8:00 PM">Last Checkpoint: a few seconds ago</span>
    <span class="autosave_status">(autosaved)</span>
</span>


  

<span id="kernel_logo_widget">
  
  <img class="current_kernel_logo" alt="Current Kernel Logo" src="./Assignment Day1_files/logo-64x64.png" title="Python 3" style="display: inline;">
  
</span>


  
  
  
  

    <span id="login_widget">
      
        <button id="logout" class="btn btn-sm navbar-btn">Logout</button>
      
    </span>

  

  
  
  </div>
  <div class="header-bar"></div>

  
<div id="menubar-container" class="container">
<div id="menubar">
    <div id="menus" class="navbar navbar-default" role="navigation">
        <div class="container-fluid">
            <button type="button" class="btn btn-default navbar-btn navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
              <i class="fa fa-bars"></i>
              <span class="navbar-text">Menu</span>
            </button>
            <p id="kernel_indicator" class="navbar-text indicator_area">
              <span class="kernel_indicator_name">Python 3</span>
              <i id="kernel_indicator_icon" class="kernel_idle_icon" title="Kernel Idle"></i>
            </p>
            <i id="readonly-indicator" class="navbar-text" title="This notebook is read-only" style="display: none;">
                <span class="fa-stack">
                    <i class="fa fa-save fa-stack-1x"></i>
                    <i class="fa fa-ban fa-stack-2x text-danger"></i>
                </span>
            </i>
            <i id="modal_indicator" class="navbar-text modal_indicator" title="Command Mode"></i>
            <span id="notification_area"><div id="notification_kernel" class="notification_widget btn btn-xs navbar-btn undefined info" style="display: none;"><span></span></div><div id="notification_notebook" class="notification_widget btn btn-xs navbar-btn" style="display: none;"><span></span></div><div id="notification_trusted" class="notification_widget btn btn-xs navbar-btn" style="cursor: help;" disabled="disabled"><span title="Javascript enabled for notebook display">Trusted</span></div><div id="notification_widgets" class="notification_widget btn btn-xs navbar-btn" style="display: none;"><span></span></div></span>
            <div class="navbar-collapse collapse">
              <ul class="nav navbar-nav">
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" id="filelink" aria-haspopup="true" aria-controls="file_menu class=" dropdown-toggle"="" data-toggle="dropdown">File</a>
                    <ul id="file_menu" class="dropdown-menu" role="menu" aria-labelledby="filelink">
                        <li id="new_notebook" class="dropdown-submenu" role="none">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">New Notebook<span class="sr-only">Toggle Dropdown</span></a>
                            <ul class="dropdown-menu" id="menu-new-notebook-submenu"><li id="new-notebook-submenu-python3"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Python 3</a></li></ul>
                        </li>
                        <li id="open_notebook" role="none" title="Opens a new window with the Dashboard view">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Open...</a></li>
                        <!-- <hr/> -->
                        <li class="divider" role="none"></li>
                        <li id="copy_notebook" role="none" title="Open a copy of this notebook&#39;s contents and start a new kernel">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Make a Copy...</a></li>
                        <li id="save_notebook_as" role="none" title="Save a copy of the notebook&#39;s contents and start a new kernel">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Save as...</a></li>
                        <li id="rename_notebook" role="none"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Rename...</a></li>
                        <li id="save_checkpoint" role="none"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Save and Checkpoint</a></li>
                        <!-- <hr/> -->
                        <li class="divider" role="none"></li>
                        <li id="restore_checkpoint" class="dropdown-submenu" role="none"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Revert to Checkpoint<span class="sr-only">Toggle Dropdown</span></a>
                          <ul class="dropdown-menu"><li><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Tuesday, July 6, 2021 8:00 PM</a></li></ul>
                        </li>
                        <li class="divider" role="none"></li>
                        <li id="print_preview" role="none"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Print Preview</a></li>
                        <li class="dropdown-submenu" role="none"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Download as<span class="sr-only">Toggle Dropdown</span></a>
                            <ul id="download_menu" class="dropdown-menu">
                                
                                <li id="download_asciidoc">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">AsciiDoc (.asciidoc)</a>
                                </li>
                                
                                <li id="download_html">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">HTML (.html)</a>
                                </li>
                                
                                <li id="download_latex">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">LaTeX (.tex)</a>
                                </li>
                                
                                <li id="download_markdown">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Markdown (.md)</a>
                                </li>
                                
                                <li id="download_notebook">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Notebook (.ipynb)</a>
                                </li>
                                
                                <li id="download_pdf">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">PDF via LaTeX (.pdf)</a>
                                </li>
                                
                                <li id="download_rst">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">reST (.rst)</a>
                                </li>
                                
                                <li id="download_script">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Python (.py)</a>
                                </li>
                                
                                <li id="download_slides">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Reveal.js slides (.slides.html)</a>
                                </li>
                                
                            </ul>
                        </li>
                        <li class="dropdown-submenu hidden" role="none"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Deploy as</a>
                            <ul id="deploy_menu" class="dropdown-menu"></ul>
                        </li>
                        <li class="divider" role="none"></li>
                        <li id="trust_notebook" role="none" title="Trust the output of this notebook" class="disabled">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Trusted Notebook</a></li>
                        <li class="divider" role="none"></li>
                        <li id="close_and_halt" role="none" title="Shutdown this notebook&#39;s kernel, and close this window">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Close and Halt</a></li>
                    </ul>
                </li>

                <li class="dropdown"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" class="dropdown-toggle" id="editlink" data-toggle="dropdown" aria-haspopup="true" aria-controls="edit_menu">Edit</a>
                    <ul id="edit_menu" class="dropdown-menu" role="menu" aria-labelledby="editlink">
                        <li id="cut_cell" role="none"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Cut Cells</a></li>
                        <li id="copy_cell" role="none"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Copy Cells</a></li>
                        <li id="paste_cell_above" class="" role="none"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem" aria-disabled="false">Paste Cells Above</a></li>
                        <li id="paste_cell_below" class="" role="none"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem" aria-disabled="false">Paste Cells Below</a></li>
                        <li id="paste_cell_replace" class="" role="none"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem" aria-disabled="false">Paste Cells &amp; Replace</a></li>
                        <li id="delete_cell" role="none"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Delete Cells</a></li>
                        <li id="undelete_cell" class="disabled" role="none"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem" aria-disabled="true">Undo Delete Cells</a></li>
                        <li class="divider" role="none"></li>
                        <li id="split_cell" role="none"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Split Cell</a></li>
                        <li id="merge_cell_above" role="none"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Merge Cell Above</a></li>
                        <li id="merge_cell_below" role="none"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Merge Cell Below</a></li>
                        <li class="divider" role="none"></li>
                        <li id="move_cell_up" role="none"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Move Cell Up</a></li>
                        <li id="move_cell_down" role="none"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Move Cell Down</a></li>
                        <li class="divider" role="none"></li>
                        <li id="edit_nb_metadata" role="none"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Edit Notebook Metadata</a></li>
                        <li class="divider" role="none"></li>
                        <li id="find_and_replace" role="none"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem"> Find and Replace </a></li>
                        <li class="divider" role="none"></li>
                        <li id="cut_cell_attachments" role="none"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Cut Cell Attachments</a></li>
                        <li id="copy_cell_attachments" role="none"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Copy Cell Attachments</a></li>
                        <li id="paste_cell_attachments" class="disabled" role="none"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem" aria-disabled="true">Paste Cell Attachments</a></li>
                        <li class="divider" role="none"></li>
                        <li id="insert_image" class="disabled" role="none"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem" aria-disabled="true">  Insert Image </a></li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" class="dropdown-toggle" id="viewlink" data-toggle="dropdown" aria-haspopup="true" aria-controls="view_menu">View</a>
                    <ul id="view_menu" class="dropdown-menu" role="menu" aria-labelledby="viewlink">
                        <li id="toggle_header" role="none" title="Show/Hide the logo and notebook title (above menu bar)">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Toggle Header</a>
                        </li>
                        <li id="toggle_toolbar" role="none" title="Show/Hide the action icons (below menu bar)">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Toggle Toolbar</a>
                        </li>
                        <li id="toggle_line_numbers" role="none" title="Show/Hide line numbers in cells">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Toggle Line Numbers</a>
                        </li>
                        <li id="menu-cell-toolbar" class="dropdown-submenu" role="none">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Cell Toolbar</a>
                            <ul class="dropdown-menu" id="menu-cell-toolbar-submenu"><li data-name="None"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">None</a></li><li data-name="Edit%20Metadata"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Edit Metadata</a></li><li data-name="Raw%20Cell%20Format"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Raw Cell Format</a></li><li data-name="Slideshow"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Slideshow</a></li><li data-name="Attachments"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Attachments</a></li><li data-name="Tags"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Tags</a></li></ul>
                        </li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" class="dropdown-toggle" id="insertlink" data-toggle="dropdown" aria-haspopup="true" aria-controls="insert_menu">Insert</a>
                    <ul id="insert_menu" class="dropdown-menu" role="menu" aria-labelledby="insertlink">
                        <li id="insert_cell_above" role="none" title="Insert an empty Code cell above the currently active cell">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Insert Cell Above</a></li>
                        <li id="insert_cell_below" role="none" title="Insert an empty Code cell below the currently active cell">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="menuitem">Insert Cell Below</a></li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" class="dropdown-toggle" data-toggle="dropdown">Cell</a>
                    <ul id="cell_menu" class="dropdown-menu">
                        <li id="run_cell" title="Run this cell, and move cursor to the next one">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Run Cells</a></li>
                        <li id="run_cell_select_below" title="Run this cell, select below">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Run Cells and Select Below</a></li>
                        <li id="run_cell_insert_below" title="Run this cell, insert below">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Run Cells and Insert Below</a></li>
                        <li id="run_all_cells" title="Run all cells in the notebook">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Run All</a></li>
                        <li id="run_all_cells_above" title="Run all cells above (but not including) this cell">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Run All Above</a></li>
                        <li id="run_all_cells_below" title="Run this cell and all cells below it">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Run All Below</a></li>
                        <li class="divider"></li>
                        <li id="change_cell_type" class="dropdown-submenu" title="All cells in the notebook have a cell type. By default, new cells are created as &#39;Code&#39; cells">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Cell Type</a>
                            <ul class="dropdown-menu">
                              <li id="to_code" title="Contents will be sent to the kernel for execution, and output will display in the footer of cell">
                                  <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Code</a></li>
                              <li id="to_markdown" title="Contents will be rendered as HTML and serve as explanatory text">
                                  <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Markdown</a></li>
                              <li id="to_raw" title="Contents will pass through nbconvert unmodified">
                                  <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Raw NBConvert</a></li>
                            </ul>
                        </li>
                        <li class="divider"></li>
                        <li id="current_outputs" class="dropdown-submenu"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Current Outputs</a>
                            <ul class="dropdown-menu">
                                <li id="toggle_current_output" title="Hide/Show the output of the current cell">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Toggle</a>
                                </li>
                                <li id="toggle_current_output_scroll" title="Scroll the output of the current cell">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Toggle Scrolling</a>
                                </li>
                                <li id="clear_current_output" title="Clear the output of the current cell">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Clear</a>
                                </li>
                            </ul>
                        </li>
                        <li id="all_outputs" class="dropdown-submenu"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">All Output</a>
                            <ul class="dropdown-menu">
                                <li id="toggle_all_output" title="Hide/Show the output of all cells">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Toggle</a>
                                </li>
                                <li id="toggle_all_output_scroll" title="Scroll the output of all cells">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Toggle Scrolling</a>
                                </li>
                                <li id="clear_all_output" title="Clear the output of all cells">
                                    <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Clear</a>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" class="dropdown-toggle" data-toggle="dropdown" id="kernellink">Kernel</a>
                    <ul id="kernel_menu" class="dropdown-menu" aria-labelledby="kernellink">
                        <li id="int_kernel" title="Send Keyboard Interrupt (CTRL-C) to the Kernel">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Interrupt</a>
                        </li>
                        <li id="restart_kernel" title="Restart the Kernel">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Restart</a>
                        </li>
                        <li id="restart_clear_output" title="Restart the Kernel and clear all output">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Restart &amp; Clear Output</a>
                        </li>
                        <li id="restart_run_all" title="Restart the Kernel and re-run the notebook">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Restart &amp; Run All</a>
                        </li>
                        <li id="reconnect_kernel" title="Reconnect to the Kernel">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Reconnect</a>
                        </li>
                        <li id="shutdown_kernel" title="Shutdown the Kernel">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Shutdown</a>
                        </li>
                        <li class="divider"></li>
                        <li id="menu-change-kernel" class="dropdown-submenu">
                            <a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Change kernel</a>
                            <ul class="dropdown-menu" id="menu-change-kernel-submenu"><li id="kernel-submenu-python3"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Python 3</a></li></ul>
                        </li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" data-toggle="dropdown" class="dropdown-toggle">Widgets</a><ul id="widget-submenu" class="dropdown-menu"><li title="Save the notebook with the widget state information for static rendering"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Save Notebook Widget State</a></li><li title="Clear the widget state information from the notebook"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Clear Notebook Widget State</a></li><ul class="divider"></ul><li title="Download the widget state as a JSON file"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Download Widget State</a></li><li title="Embed interactive widgets"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Embed Widgets</a></li></ul></li><li class="dropdown"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" class="dropdown-toggle" data-toggle="dropdown">Help</a>
                    <ul id="help_menu" class="dropdown-menu">
                        
                        <li id="notebook_tour" title="A quick tour of the notebook user interface"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">User Interface Tour</a></li>
                        <li id="keyboard_shortcuts" title="Opens a tooltip with all keyboard shortcuts"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Keyboard Shortcuts</a></li>
                        <li id="edit_keyboard_shortcuts" title="Opens a dialog allowing you to edit Keyboard shortcuts"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">Edit Keyboard Shortcuts</a></li>
                        <li class="divider"></li>
                        

						
                        
                            
                                <li><a rel="noreferrer" href="http://nbviewer.jupyter.org/github/ipython/ipython/blob/3.x/examples/Notebook/Index.ipynb" target="_blank" title="Opens in a new window">
                                
                                    <i class="fa fa-external-link menu-icon pull-right"></i>
                                

                                Notebook Help
                                </a></li>
                            
                                <li><a rel="noreferrer" href="https://help.github.com/articles/markdown-basics/" target="_blank" title="Opens in a new window">
                                
                                    <i class="fa fa-external-link menu-icon pull-right"></i>
                                

                                Markdown
                                </a></li>
                            
                            
                        
                        <li id="kernel-help-links" class="divider"></li><li><a target="_blank" title="Opens in a new window" href="https://docs.python.org/3.8?v=20210706175842"><i class="fa fa-external-link menu-icon pull-right"></i><span>Python Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://ipython.org/documentation.html?v=20210706175842"><i class="fa fa-external-link menu-icon pull-right"></i><span>IPython Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://docs.scipy.org/doc/numpy/reference/?v=20210706175842"><i class="fa fa-external-link menu-icon pull-right"></i><span>NumPy Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://docs.scipy.org/doc/scipy/reference/?v=20210706175842"><i class="fa fa-external-link menu-icon pull-right"></i><span>SciPy Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://matplotlib.org/contents.html?v=20210706175842"><i class="fa fa-external-link menu-icon pull-right"></i><span>Matplotlib Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="http://docs.sympy.org/latest/index.html?v=20210706175842"><i class="fa fa-external-link menu-icon pull-right"></i><span>SymPy Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://pandas.pydata.org/pandas-docs/stable/?v=20210706175842"><i class="fa fa-external-link menu-icon pull-right"></i><span>pandas Reference</span></a></li><li class="divider"></li>
                        <li title="About Jupyter Notebook"><a id="notebook_about" href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#">About</a></li>
                        
                    </ul>
                </li>
              </ul>
            </div>
        </div>
    </div>
</div>

<div id="maintoolbar" class="navbar">
  <div class="toolbar-inner navbar-inner navbar-nobg">
    <div id="maintoolbar-container" class="container toolbar"><div class="btn-group" id="save-notbook"><button class="btn btn-default" title="Save and Checkpoint" data-jupyter-action="jupyter-notebook:save-notebook"><i class="fa-save fa"></i></button></div><div class="btn-group" id="insert_above_below"><button class="btn btn-default" title="insert cell below" data-jupyter-action="jupyter-notebook:insert-cell-below"><i class="fa-plus fa"></i></button></div><div class="btn-group" id="cut_copy_paste"><button class="btn btn-default" title="cut selected cells" data-jupyter-action="jupyter-notebook:cut-cell"><i class="fa-cut fa"></i></button><button class="btn btn-default" title="copy selected cells" data-jupyter-action="jupyter-notebook:copy-cell"><i class="fa-copy fa"></i></button><button class="btn btn-default" title="paste cells below" data-jupyter-action="jupyter-notebook:paste-cell-below"><i class="fa-paste fa"></i></button></div><div class="btn-group" id="move_up_down"><button class="btn btn-default" title="move selected cells up" data-jupyter-action="jupyter-notebook:move-cell-up"><i class="fa-arrow-up fa"></i></button><button class="btn btn-default" title="move selected cells down" data-jupyter-action="jupyter-notebook:move-cell-down"><i class="fa-arrow-down fa"></i></button></div><div class="btn-group" id="run_int"><button class="btn btn-default" title="Run" data-jupyter-action="jupyter-notebook:run-cell-and-select-next"><i class="fa-step-forward fa"></i><span class="toolbar-btn-label">Run</span></button><button class="btn btn-default" title="interrupt the kernel" data-jupyter-action="jupyter-notebook:interrupt-kernel"><i class="fa-stop fa"></i></button><button class="btn btn-default" title="restart the kernel (with dialog)" data-jupyter-action="jupyter-notebook:confirm-restart-kernel"><i class="fa-repeat fa"></i></button><button class="btn btn-default" title="restart the kernel, then re-run the whole notebook (with dialog)" data-jupyter-action="jupyter-notebook:confirm-restart-kernel-and-run-all-cells"><i class="fa-forward fa"></i></button></div><select id="cell_type" aria-label="combobox, select cell type" role="combobox" class="form-control select-xs"><option value="code">Code</option><option value="markdown">Markdown</option><option value="raw">Raw NBConvert</option><option value="heading">Heading</option><option value="multiselect" disabled="disabled" style="display: none;">-</option></select><div class="btn-group" id="cmd_palette"><button class="btn btn-default" title="open the command palette" data-jupyter-action="jupyter-notebook:show-command-palette"><i class="fa-keyboard-o fa"></i></button></div></div>
  </div>
</div>
</div>

<div class="lower-header-bar"></div>

</div>

<div id="site" style="display: block; height: 547px;">


<div id="ipython-main-app">
    <div id="notebook_panel">
        <div id="notebook" tabindex="-1"><div class="container" id="notebook-container"><div class="cell code_cell unrendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[&nbsp;]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area" aria-label="Edit code here"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 5.59375px; left: 258.109px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 261.109px; margin-bottom: -17px; border-right-width: 13px; min-height: 28px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like">x</pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 0px; width: 254.109px; height: 17px;"></div></div><div class="CodeMirror-cursors" style="visibility: hidden;"></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plot</span> <span class="cm-variable">a</span> <span class="cm-variable">line</span> <span class="cm-variable">plot</span> <span class="cm-variable">between</span> <span class="cm-variable">a</span> <span class="cm-keyword">and</span> <span class="cm-variable">b</span>:</span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 28px;"></div><div class="CodeMirror-gutters" style="display: none; height: 41px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to expand output; double click to hide output"></div><div class="output"></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[2]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area" aria-label="Edit code here"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 107.594px; left: 142.578px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 438.172px; margin-bottom: -17px; border-right-width: 13px; min-height: 147px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like">x</pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 0px; width: 985px; height: 17px;"></div><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 102px; width: 138.578px; height: 17px;"></div><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 17px; width: 985px; height: 85px;"></div></div><div class="CodeMirror-cursors" style=""></div><div class="CodeMirror-code" role="presentation" style=""><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">numpy</span> <span class="cm-keyword">as</span> <span class="cm-variable">np</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">pandas</span> <span class="cm-keyword">as</span> <span class="cm-variable">pd</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">seaborn</span> <span class="cm-keyword">as</span> <span class="cm-variable">sns</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">from</span> <span class="cm-variable">numpy</span>.<span class="cm-property">random</span> <span class="cm-keyword">import</span> <span class="cm-variable">randn</span>, <span class="cm-variable">randint</span>, <span class="cm-variable">uniform</span>, <span class="cm-variable">sample</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">matplotlib</span> <span class="cm-keyword">as</span> <span class="cm-variable">mpl</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">matplotlib</span>.<span class="cm-property">pyplot</span> <span class="cm-keyword">as</span> <span class="cm-variable">plt</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-operator">%</span><span class="cm-variable">matplotlib</span> <span class="cm-variable">inline</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">???</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 147px;"></div><div class="CodeMirror-gutters" style="display: none; height: 160px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[3]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area" aria-label="Edit code here"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 39.5938px; left: 4px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 145.625px; margin-bottom: -17px; border-right-width: 13px; min-height: 62px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like">x</pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 0px; width: 985px; height: 17px;"></div><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 34px; width: 0px; height: 17px;"></div><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 17px; width: 985px; height: 17px;"></div></div><div class="CodeMirror-cursors" style="visibility: hidden;"></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">a</span><span class="cm-operator">=</span><span class="cm-variable">np</span>.<span class="cm-property">arange</span>(<span class="cm-number">40</span>,<span class="cm-number">50</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">b</span><span class="cm-operator">=</span><span class="cm-variable">np</span>.<span class="cm-property">arange</span>(<span class="cm-number">50</span>,<span class="cm-number">60</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">???</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 62px;"></div><div class="CodeMirror-gutters" style="display: none; height: 75px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[5]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area" aria-label="Edit code here"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 56.5938px; left: 157.969px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 368.891px; margin-bottom: -17px; border-right-width: 13px; min-height: 79px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like">x</pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 0px; width: 985px; height: 17px;"></div><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 51px; width: 153.969px; height: 17px;"></div><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 17px; width: 985px; height: 34px;"></div></div><div class="CodeMirror-cursors" style="visibility: hidden;"></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">plot</span>(<span class="cm-variable">a</span>,<span class="cm-variable">b</span>,<span class="cm-string">'go--'</span>, <span class="cm-variable">linewidth</span><span class="cm-operator">=</span><span class="cm-number">1</span>, <span class="cm-variable">markersize</span><span class="cm-operator">=</span><span class="cm-number">5</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">title</span>(<span class="cm-string">'Line Plot'</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">xlabel</span>(<span class="cm-string">'a-axis'</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">ylabel</span>(<span class="cm-string">'b-axis'</span>)</span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 79px;"></div><div class="CodeMirror-gutters" style="display: none; height: 92px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"><div class="output_area"><div class="run_this_cell"></div><div class="prompt output_prompt"><bdi>Out[5]:</bdi></div><div class="output_subarea output_text output_result"><pre>Text(0, 0.5, 'b-axis')</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_png"><img src="data:image/png;base64,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"></div></div></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell unrendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[&nbsp;]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area" aria-label="Edit code here"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 5.59375px; left: 458.312px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 461.312px; margin-bottom: -17px; border-right-width: 13px; min-height: 28px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like">x</pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 0px; width: 454.312px; height: 17px;"></div></div><div class="CodeMirror-cursors" style="visibility: hidden;"></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">Plot</span> <span class="cm-variable">a</span> <span class="cm-variable">line</span> <span class="cm-variable">plot</span> <span class="cm-variable">showing</span> <span class="cm-variable">the</span> <span class="cm-variable">sales</span> <span class="cm-variable">trend</span> <span class="cm-keyword">in</span> <span class="cm-variable">company</span> <span class="cm-number">1</span> <span class="cm-keyword">and</span> <span class="cm-number">2</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 28px;"></div><div class="CodeMirror-gutters" style="display: none; height: 41px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to expand output; double click to hide output"></div><div class="output"></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[6]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area" aria-label="Edit code here"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 39.5938px; left: 288.906px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 314.984px; margin-bottom: -17px; border-right-width: 13px; min-height: 79px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like">x</pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 0px; width: 985px; height: 17px;"></div><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 34px; width: 284.906px; height: 17px;"></div><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 17px; width: 985px; height: 17px;"></div></div><div class="CodeMirror-cursors" style=""></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">days</span> <span class="cm-operator">=</span> [<span class="cm-number">1</span>,<span class="cm-number">2</span>,<span class="cm-number">3</span>,<span class="cm-number">4</span>,<span class="cm-number">5</span>,<span class="cm-number">6</span>,<span class="cm-number">7</span>] </span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">sales_1</span> <span class="cm-operator">=</span> [<span class="cm-number">160</span>,<span class="cm-number">150</span>,<span class="cm-number">140</span>,<span class="cm-number">145</span>,<span class="cm-number">175</span>,<span class="cm-number">165</span>,<span class="cm-number">180</span>] </span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">sales_2</span> <span class="cm-operator">=</span> [<span class="cm-number">70</span>,<span class="cm-number">90</span>,<span class="cm-number">160</span>,<span class="cm-number">150</span>,<span class="cm-number">140</span>,<span class="cm-number">145</span>,<span class="cm-number">175</span>]</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">???</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 79px;"></div><div class="CodeMirror-gutters" style="display: none; height: 92px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[18]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area" aria-label="Edit code here"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 192.594px; left: 81px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 538.281px; margin-bottom: -17px; border-right-width: 13px; min-height: 215px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like">x</pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 0px; width: 985px; height: 17px;"></div><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 187px; width: 77px; height: 17px;"></div><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 17px; width: 985px; height: 170px;"></div></div><div class="CodeMirror-cursors" style=""></div><div class="CodeMirror-code" role="presentation" style=""><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">figure</span>(<span class="cm-variable">figsize</span> <span class="cm-operator">=</span>(<span class="cm-number">6</span>,<span class="cm-number">5</span>), <span class="cm-variable">dpi</span><span class="cm-operator">=</span><span class="cm-number">150</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">plot</span>(<span class="cm-variable">days</span>, <span class="cm-variable">sales_1</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">plot</span>(<span class="cm-variable">days</span>, <span class="cm-variable">sales_2</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">plot</span>(<span class="cm-variable">days</span>, <span class="cm-variable">sales_1</span>, <span class="cm-variable">linewidth</span><span class="cm-operator">=</span><span class="cm-number">5</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">plot</span>(<span class="cm-variable">days</span>,<span class="cm-variable">sales_1</span>,<span class="cm-string">'ro--'</span>, <span class="cm-variable">markersize</span><span class="cm-operator">=</span><span class="cm-number">20</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">plot</span>(<span class="cm-variable">days</span>,<span class="cm-variable">sales_1</span>, <span class="cm-string">'o'</span>, <span class="cm-variable">markersize</span><span class="cm-operator">=</span><span class="cm-number">15</span>, <span class="cm-variable">color</span><span class="cm-operator">=</span><span class="cm-string">'b'</span>, <span class="cm-variable">linestyle</span><span class="cm-operator">=</span><span class="cm-string">'--'</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">plot</span>(<span class="cm-variable">days</span>,<span class="cm-variable">sales_2</span>, <span class="cm-string">'*'</span>, <span class="cm-variable">markersize</span><span class="cm-operator">=</span><span class="cm-number">15</span>, <span class="cm-variable">color</span><span class="cm-operator">=</span><span class="cm-string">'r'</span>, <span class="cm-variable">linestyle</span><span class="cm-operator">=</span><span class="cm-string">'--'</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">title</span>(<span class="cm-string">'sales per day in USD'</span>,<span class="cm-variable">fontsize</span><span class="cm-operator">=</span><span class="cm-number">10</span>,<span class="cm-variable">color</span><span class="cm-operator">=</span><span class="cm-string">"blue"</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">xlabel</span>(<span class="cm-string">"Days of the Week"</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">ylabel</span>(<span class="cm-string">"sales"</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">grid</span>()</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">show</span>()</span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 215px;"></div><div class="CodeMirror-gutters" style="display: none; height: 228px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_png"><img src="data:image/png;base64,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"></div></div></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell unrendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[&nbsp;]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area" aria-label="Edit code here"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 5.59375px; left: 319.688px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 322.688px; margin-bottom: -17px; border-right-width: 13px; min-height: 28px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like">x</pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 0px; width: 315.688px; height: 17px;"></div></div><div class="CodeMirror-cursors" style="visibility: hidden;"></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> <span class="cm-variable">Create</span> <span class="cm-variable">a</span> <span class="cm-number">3</span> <span class="cm-variable">by</span> <span class="cm-number">3</span> <span class="cm-variable">subplots</span> <span class="cm-variable">multiple</span> <span class="cm-variable">plots</span>:</span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 28px;"></div><div class="CodeMirror-gutters" style="display: none; height: 41px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to expand output; double click to hide output"></div><div class="output"></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell rendered selected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[25]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area" aria-label="Edit code here"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 260.594px; left: 150.312px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 168.703px; margin-bottom: -17px; border-right-width: 13px; min-height: 283px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like">x</pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 0px; width: 985px; height: 17px;"></div><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 255px; width: 146.312px; height: 17px;"></div><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 17px; width: 985px; height: 238px;"></div></div><div class="CodeMirror-cursors" style="visibility: hidden;"></div><div class="CodeMirror-code" role="presentation" style=""><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">x</span> <span class="cm-operator">=</span> [<span class="cm-number">1</span>,<span class="cm-number">2</span>,<span class="cm-number">3</span>,<span class="cm-number">4</span>]</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">y1</span> <span class="cm-operator">=</span> [<span class="cm-number">4</span>,<span class="cm-number">3</span>,<span class="cm-number">2</span>,<span class="cm-number">1</span>]</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">y2</span> <span class="cm-operator">=</span> [<span class="cm-number">10</span>,<span class="cm-number">20</span>,<span class="cm-number">30</span>,<span class="cm-number">40</span>]</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">y3</span> <span class="cm-operator">=</span> [<span class="cm-number">40</span>,<span class="cm-number">30</span>,<span class="cm-number">20</span>,<span class="cm-number">10</span>]</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">y4</span> <span class="cm-operator">=</span> [<span class="cm-number">1</span>,<span class="cm-number">2</span>,<span class="cm-number">1</span>,<span class="cm-number">2</span>]</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">y5</span> <span class="cm-operator">=</span> [<span class="cm-number">40</span>,<span class="cm-number">70</span>,<span class="cm-number">90</span>,<span class="cm-number">70</span>]</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">???</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">subplot</span>(<span class="cm-number">2</span>,<span class="cm-number">2</span>,<span class="cm-number">1</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">plot</span>(<span class="cm-variable">x</span>,<span class="cm-variable">y1</span>,<span class="cm-string">'r--'</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">subplot</span>(<span class="cm-number">2</span>,<span class="cm-number">2</span>,<span class="cm-number">2</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">plot</span>(<span class="cm-variable">x</span>,<span class="cm-variable">y2</span>,<span class="cm-string">'g*--'</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">subplot</span>(<span class="cm-number">2</span>,<span class="cm-number">2</span>,<span class="cm-number">3</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">plot</span>(<span class="cm-variable">x</span>,<span class="cm-variable">y3</span>,<span class="cm-string">'bo--'</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">subplot</span>(<span class="cm-number">2</span>,<span class="cm-number">2</span>,<span class="cm-number">4</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">plot</span>(<span class="cm-variable">x</span>,<span class="cm-variable">y4</span>,<span class="cm-string">'go--'</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">plot</span>(<span class="cm-variable">x</span>,<span class="cm-variable">y5</span>,<span class="cm-string">'b*'</span>)</span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 283px;"></div><div class="CodeMirror-gutters" style="display: none; height: 296px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"><div class="output_area"><div class="run_this_cell"></div><div class="prompt output_prompt"><bdi>Out[25]:</bdi></div><div class="output_subarea output_text output_result"><pre>[&lt;matplotlib.lines.Line2D at 0x1e9430a60d0&gt;]</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_png"><img src="data:image/png;base64,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"></div></div></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell unrendered unselected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[&nbsp;]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area" aria-label="Edit code here"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 5.59375px; left: 4px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 7px; margin-bottom: -17px; border-right-width: 13px; min-height: 28px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style="visibility: hidden;"><div class="CodeMirror-cursor" style="left: 4px; top: 0px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">???</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 28px;"></div><div class="CodeMirror-gutters" style="display: none; height: 41px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to expand output; double click to hide output"></div><div class="output"></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div></div><div class="end_space"></div></div>
        <div id="tooltip" class="ipython_tooltip" style="left: 228.438px; top: 2024.06px; display: none;"><div class="tooltipbuttons"><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="button" class="ui-button"><span class="ui-icon ui-icon-close">Close</span></a><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="button" class="ui-button" id="expanbutton" title="Grow the tooltip vertically (press shift-tab twice)" style=""><span class="ui-icon ui-icon-plus">Expand</span></a><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="button" class="ui-button" title="show the current docstring in pager (press shift-tab 4 times)"><span class="ui-icon ui-icon-arrowstop-l-n">Open in Pager</span></a><a href="http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3#" role="button" class="ui-button" title="Tooltip will linger for 10 seconds while you type" style="display: none;"><span class="ui-icon ui-icon-clock">Close</span></a></div><div class="pretooltiparrow" style="left: 95.5px;"></div><div class="tooltiptext smalltooltip"><pre><span class="ansi-red-intense-fg ansi-bold">Signature:</span> plt<span class="ansi-yellow-intense-fg ansi-bold">.</span>subplot<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">*</span>args<span class="ansi-yellow-intense-fg ansi-bold">,</span> <span class="ansi-yellow-intense-fg ansi-bold">**</span>kwargs<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-red-intense-fg ansi-bold">Docstring:</span>
Add a subplot to the current figure.

Wrapper of `.Figure.add_subplot` with a difference in behavior
explained in the notes section.

Call signatures::

   subplot(nrows, ncols, index, **kwargs)
   subplot(pos, **kwargs)
   subplot(ax)

Parameters
----------
*args
    Either a 3-digit integer or three separate integers
    describing the position of the subplot. If the three
    integers are *nrows*, *ncols*, and *index* in order, the
    subplot will take the *index* position on a grid with *nrows*
    rows and *ncols* columns. *index* starts at 1 in the upper left
    corner and increases to the right.

    *pos* is a three digit integer, where the first digit is the
    number of rows, the second the number of columns, and the third
    the index of the subplot. i.e. fig.add_subplot(235) is the same as
    fig.add_subplot(2, 3, 5). Note that all integers must be less than
    10 for this form to work.

projection : {None, 'aitoff', 'hammer', 'lambert', 'mollweide', 'polar', 'rectilinear', str}, optional
    The projection type of the subplot (`~.axes.Axes`). *str* is the name
    of a custom projection, see `~matplotlib.projections`. The default
    None results in a 'rectilinear' projection.

polar : boolean, optional
    If True, equivalent to projection='polar'.

sharex, sharey : `~.axes.Axes`, optional
    Share the x or y `~matplotlib.axis` with sharex and/or sharey. The
    axis will have the same limits, ticks, and scale as the axis of the
    shared axes.

label : str
    A label for the returned axes.

Other Parameters
----------------
**kwargs
    This method also takes the keyword arguments for the returned axes
    base class; except for the *figure* argument. The keyword arguments
    for the rectilinear base class `~.axes.Axes` can be found in
    the following table but there might also be other keyword
    arguments if another projection is used.

    Properties:
    adjustable: {'box', 'datalim'}
    agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array
    alpha: float or None
    anchor: 2-tuple of floats or {'C', 'SW', 'S', 'SE', ...}
    animated: bool
    aspect: {'auto', 'equal'} or num
    autoscale_on: bool
    autoscalex_on: bool
    autoscaley_on: bool
    axes_locator: Callable[[Axes, Renderer], Bbox]
    axisbelow: bool or 'line'
    clip_box: `.Bbox`
    clip_on: bool
    clip_path: Patch or (Path, Transform) or None
    contains: callable
    facecolor: color
    fc: color
    figure: `.Figure`
    frame_on: bool
    gid: str
    in_layout: bool
    label: object
    navigate: bool
    navigate_mode: unknown
    path_effects: `.AbstractPathEffect`
    picker: None or bool or float or callable
    position: [left, bottom, width, height] or `~matplotlib.transforms.Bbox`
    prop_cycle: unknown
    rasterization_zorder: float or None
    rasterized: bool or None
    sketch_params: (scale: float, length: float, randomness: float)
    snap: bool or None
    title: str
    transform: `.Transform`
    url: str
    visible: bool
    xbound: unknown
    xlabel: str
    xlim: (bottom: float, top: float)
    xmargin: float greater than -0.5
    xscale: {"linear", "log", "symlog", "logit", ...}
    xticklabels: List[str]
    xticks: unknown
    ybound: unknown
    ylabel: str
    ylim: (bottom: float, top: float)
    ymargin: float greater than -0.5
    yscale: {"linear", "log", "symlog", "logit", ...}
    yticklabels: List[str]
    yticks: unknown
    zorder: float

Returns
-------
axes : an `.axes.SubplotBase` subclass of `~.axes.Axes` (or a subclass     of `~.axes.Axes`)

    The axes of the subplot. The returned axes base class depends on
    the projection used. It is `~.axes.Axes` if rectilinear projection
    are used and `.projections.polar.PolarAxes` if polar projection
    are used. The returned axes is then a subplot subclass of the
    base class.

Notes
-----
Creating a subplot will delete any pre-existing subplot that overlaps
with it beyond sharing a boundary::

    import matplotlib.pyplot as plt
    # plot a line, implicitly creating a subplot(111)
    plt.plot([1, 2, 3])
    # now create a subplot which represents the top plot of a grid
    # with 2 rows and 1 column. Since this subplot will overlap the
    # first, the plot (and its axes) previously created, will be removed
    plt.subplot(211)

If you do not want this behavior, use the `.Figure.add_subplot` method
or the `.pyplot.axes` function instead.

If the figure already has a subplot with key (*args*,
*kwargs*) then it will simply make that subplot current and
return it.  This behavior is deprecated. Meanwhile, if you do
not want this behavior (i.e., you want to force the creation of a
new subplot), you must use a unique set of args and kwargs.  The axes
*label* attribute has been exposed for this purpose: if you want
two subplots that are otherwise identical to be added to the figure,
make sure you give them unique labels.

In rare circumstances, `.add_subplot` may be called with a single
argument, a subplot axes instance already created in the
present figure but not in the figure's list of axes.

See Also
--------
.Figure.add_subplot
.pyplot.subplots
.pyplot.axes
.Figure.subplots

Examples
--------
::

    plt.subplot(221)

    # equivalent but more general
    ax1=plt.subplot(2, 2, 1)

    # add a subplot with no frame
    ax2=plt.subplot(222, frameon=False)

    # add a polar subplot
    plt.subplot(223, projection='polar')

    # add a red subplot that shares the x-axis with ax1
    plt.subplot(224, sharex=ax1, facecolor='red')

    # delete ax2 from the figure
    plt.delaxes(ax2)

    # add ax2 to the figure again
    plt.subplot(ax2)
<span class="ansi-red-intense-fg ansi-bold">File:</span>      c:\users\jagunu\anaconda\lib\site-packages\matplotlib\pyplot.py
<span class="ansi-red-intense-fg ansi-bold">Type:</span>      function
</pre></div></div>
    </div>
</div>



</div>



<div id="pager" class="ui-resizable">
    <div id="pager-contents">
        <div id="pager-container" class="container"></div>
    </div>
    <div id="pager-button-area"><a role="button" title="Open the pager in an external window" class="ui-button"><span class="ui-icon ui-icon-extlink"></span></a><a role="button" title="Close the pager" class="ui-button"><span class="ui-icon ui-icon-close"></span></a></div>
<div class="ui-resizable-handle ui-resizable-n" style="z-index: 90;"></div></div>






<script type="text/javascript">
    sys_info = {"notebook_version": "6.0.3", "notebook_path": "C:\\Users\\Jagunu\\anaconda\\Lib\\site-packages\\notebook", "commit_source": "", "commit_hash": "", "sys_version": "3.8.3 (default, Jul  2 2020, 17:30:36) [MSC v.1916 64 bit (AMD64)]", "sys_executable": "C:\\Users\\Jagunu\\anaconda\\python.exe", "sys_platform": "win32", "platform": "Windows-10-10.0.19041-SP0", "os_name": "nt", "default_encoding": "utf-8"};
</script>

<script src="./Assignment Day1_files/encoding.js.download" charset="utf-8"></script>

<script src="./Assignment Day1_files/main.min.js.download" type="text/javascript" charset="utf-8"></script>



<script type="text/javascript">
  function _remove_token_from_url() {
    if (window.location.search.length <= 1) {
      return;
    }
    var search_parameters = window.location.search.slice(1).split('&');
    for (var i = 0; i < search_parameters.length; i++) {
      if (search_parameters[i].split('=')[0] === 'token') {
        // remote token from search parameters
        search_parameters.splice(i, 1);
        var new_search = '';
        if (search_parameters.length) {
          new_search = '?' + search_parameters.join('&');
        }
        var new_url = window.location.origin + 
                      window.location.pathname + 
                      new_search + 
                      window.location.hash;
        window.history.replaceState({}, "", new_url);
        return;
      }
    }
  }
  _remove_token_from_url();
</script>


<div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal;"></div></div><div class="modal cmd-palette" style="display: none;"><div class="modal-dialog"><div class="modal-content"><div class="modal-body"><form><div class="typeahead__container"><div class="typeahead__field"><span class="typeahead__query" style="position: relative;"><span class="typeahead__cancel-button">??</span><input type="search"><input type="search" readonly="readonly" unselectable="on" aria-hidden="true" tabindex="-1" class="typeahead__hint" style="border-color: transparent; position: absolute; top: 0px; display: inline; z-index: -1; float: none; color: rgb(192, 192, 192); box-shadow: none; cursor: default; user-select: none;"></span><span class="typeahead__button"><button type="submit"><span class="typeahead__search-icon"></span></button></span></div><div class="typeahead__result"><ul class="typeahead__list"><li class="typeahead__group" data-search-group="jupyter-notebook"><a href="javascript:;" tabindex="-1">jupyter-notebook command group</a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="0"><a href="javascript:;"><i class="fa fa-icon "></i>automatically indent selection  <div title="jupyter-notebook:auto-indent" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="1"><a href="javascript:;"><i class="fa fa-icon "></i>change cell to code  <div title="jupyter-notebook:change-cell-to-code" class="pull-right command-shortcut"><kbd>Y</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="2"><a href="javascript:;"><i class="fa fa-icon "></i>change cell to heading 1  <div title="jupyter-notebook:change-cell-to-heading-1" class="pull-right command-shortcut"><kbd>1</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="3"><a href="javascript:;"><i class="fa fa-icon "></i>change cell to heading 2  <div title="jupyter-notebook:change-cell-to-heading-2" class="pull-right command-shortcut"><kbd>2</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="4"><a href="javascript:;"><i class="fa fa-icon "></i>change cell to heading 3  <div title="jupyter-notebook:change-cell-to-heading-3" class="pull-right command-shortcut"><kbd>3</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="5"><a href="javascript:;"><i class="fa fa-icon "></i>change cell to heading 4  <div title="jupyter-notebook:change-cell-to-heading-4" class="pull-right command-shortcut"><kbd>4</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="6"><a href="javascript:;"><i class="fa fa-icon "></i>change cell to heading 5  <div title="jupyter-notebook:change-cell-to-heading-5" class="pull-right command-shortcut"><kbd>5</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="7"><a href="javascript:;"><i class="fa fa-icon "></i>change cell to heading 6  <div title="jupyter-notebook:change-cell-to-heading-6" class="pull-right command-shortcut"><kbd>6</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="8"><a href="javascript:;"><i class="fa fa-icon "></i>change cell to markdown  <div title="jupyter-notebook:change-cell-to-markdown" class="pull-right command-shortcut"><kbd>M</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="9"><a href="javascript:;"><i class="fa fa-icon "></i>change cell to raw  <div title="jupyter-notebook:change-cell-to-raw" class="pull-right command-shortcut"><kbd>R</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="10"><a href="javascript:;"><i class="fa fa-icon "></i>clear all cells output  <div title="jupyter-notebook:clear-all-cells-output" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="11"><a href="javascript:;"><i class="fa fa-icon "></i>clear cell output  <div title="jupyter-notebook:clear-cell-output" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="12"><a href="javascript:;"><i class="fa fa-icon "></i>close the pager  <div title="jupyter-notebook:close-pager" class="pull-right command-shortcut"><kbd>Esc</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="13"><a href="javascript:;"><i class="fa fa-icon fa-repeat"></i>confirm restart kernel  <div title="jupyter-notebook:confirm-restart-kernel" class="pull-right command-shortcut"><kbd>0</kbd>,<kbd>0</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="14"><a href="javascript:;"><i class="fa fa-icon "></i>confirm restart kernel and clear output  <div title="jupyter-notebook:confirm-restart-kernel-and-clear-output" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="15"><a href="javascript:;"><i class="fa fa-icon fa-forward"></i>confirm restart kernel and run all cells  <div title="jupyter-notebook:confirm-restart-kernel-and-run-all-cells" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="16"><a href="javascript:;"><i class="fa fa-icon fa-repeat"></i>confirm shutdown kernel  <div title="jupyter-notebook:confirm-shutdown-kernel" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="17"><a href="javascript:;"><i class="fa fa-icon "></i>copy cell attachments  <div title="jupyter-notebook:copy-cell-attachments" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="18"><a href="javascript:;"><i class="fa fa-icon fa-copy"></i>copy selected cells  <div title="jupyter-notebook:copy-cell" class="pull-right command-shortcut"><kbd>C</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="19"><a href="javascript:;"><i class="fa fa-icon "></i>cut cell attachments  <div title="jupyter-notebook:cut-cell-attachments" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="20"><a href="javascript:;"><i class="fa fa-icon fa-cut"></i>cut selected cells  <div title="jupyter-notebook:cut-cell" class="pull-right command-shortcut"><kbd>X</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="21"><a href="javascript:;"><i class="fa fa-icon "></i>delete cells  <div title="jupyter-notebook:delete-cell" class="pull-right command-shortcut"><kbd>D</kbd>,<kbd>D</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="22"><a href="javascript:;"><i class="fa fa-icon "></i>duplicate notebook  <div title="jupyter-notebook:duplicate-notebook" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="23"><a href="javascript:;"><i class="fa fa-icon "></i>edit command mode keyboard shortcuts  <div title="jupyter-notebook:edit-command-mode-keyboard-shortcuts" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="24"><a href="javascript:;"><i class="fa fa-icon "></i>enter command mode  <div title="jupyter-notebook:enter-command-mode" class="pull-right edit-shortcut"><kbd>Esc</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="25"><a href="javascript:;"><i class="fa fa-icon "></i>enter edit mode  <div title="jupyter-notebook:enter-edit-mode" class="pull-right command-shortcut"><kbd>Enter</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="26"><a href="javascript:;"><i class="fa fa-icon "></i>extend selection above  <div title="jupyter-notebook:extend-selection-above" class="pull-right command-shortcut"><kbd>Shift-K</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="27"><a href="javascript:;"><i class="fa fa-icon "></i>extend selection below  <div title="jupyter-notebook:extend-selection-below" class="pull-right command-shortcut"><kbd>Shift-J</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="28"><a href="javascript:;"><i class="fa fa-icon "></i>find and replace  <div title="jupyter-notebook:find-and-replace" class="pull-right command-shortcut"><kbd>F</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="29"><a href="javascript:;"><i class="fa fa-icon "></i>hide all line numbers  <div title="jupyter-notebook:hide-all-line-numbers" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="30"><a href="javascript:;"><i class="fa fa-icon "></i>hide menubar  <div title="jupyter-notebook:hide-menubar" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="31"><a href="javascript:;"><i class="fa fa-icon "></i>hide the header  <div title="jupyter-notebook:hide-header" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="32"><a href="javascript:;"><i class="fa fa-icon "></i>hide the toolbar  <div title="jupyter-notebook:hide-toolbar" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="33"><a href="javascript:;"><i class="fa fa-icon "></i>ignore  <div title="jupyter-notebook:ignore" class="pull-right command-shortcut"><kbd>Shift</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="34"><a href="javascript:;"><i class="fa fa-icon "></i>insert cell above  <div title="jupyter-notebook:insert-cell-above" class="pull-right command-shortcut"><kbd>A</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="35"><a href="javascript:;"><i class="fa fa-icon fa-plus"></i>insert cell below  <div title="jupyter-notebook:insert-cell-below" class="pull-right command-shortcut"><kbd>B</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="36"><a href="javascript:;"><i class="fa fa-icon "></i>insert image  <div title="jupyter-notebook:insert-image" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="37"><a href="javascript:;"><i class="fa fa-icon fa-stop"></i>interrupt the kernel  <div title="jupyter-notebook:interrupt-kernel" class="pull-right command-shortcut"><kbd>I</kbd>,<kbd>I</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="38"><a href="javascript:;"><i class="fa fa-icon "></i>merge cell with next cell  <div title="jupyter-notebook:merge-cell-with-next-cell" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="39"><a href="javascript:;"><i class="fa fa-icon "></i>merge cell with previous cell  <div title="jupyter-notebook:merge-cell-with-previous-cell" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="40"><a href="javascript:;"><i class="fa fa-icon "></i>merge cells  <div title="jupyter-notebook:merge-cells" class="pull-right command-shortcut"><kbd>Shift-M</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="41"><a href="javascript:;"><i class="fa fa-icon "></i>merge selected cells  <div title="jupyter-notebook:merge-selected-cells" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="42"><a href="javascript:;"><i class="fa fa-icon fa-arrow-down"></i>move cells down  <div title="jupyter-notebook:move-cell-down" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="43"><a href="javascript:;"><i class="fa fa-icon fa-arrow-up"></i>move cells up  <div title="jupyter-notebook:move-cell-up" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="44"><a href="javascript:;"><i class="fa fa-icon "></i>move cursor down  <div title="jupyter-notebook:move-cursor-down" class="pull-right edit-shortcut"><kbd>Down</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="45"><a href="javascript:;"><i class="fa fa-icon "></i>move cursor up  <div title="jupyter-notebook:move-cursor-up" class="pull-right edit-shortcut"><kbd>Up</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="46"><a href="javascript:;"><i class="fa fa-icon "></i>paste cell attachments  <div title="jupyter-notebook:paste-cell-attachments" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="47"><a href="javascript:;"><i class="fa fa-icon "></i>paste cell replace  <div title="jupyter-notebook:paste-cell-replace" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="48"><a href="javascript:;"><i class="fa fa-icon "></i>paste cells above  <div title="jupyter-notebook:paste-cell-above" class="pull-right command-shortcut"><kbd>Shift-V</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="49"><a href="javascript:;"><i class="fa fa-icon fa-paste"></i>paste cells below  <div title="jupyter-notebook:paste-cell-below" class="pull-right command-shortcut"><kbd>V</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="50"><a href="javascript:;"><i class="fa fa-icon "></i>rename notebook  <div title="jupyter-notebook:rename-notebook" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="51"><a href="javascript:;"><i class="fa fa-icon "></i>restart kernel  <div title="jupyter-notebook:restart-kernel" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="52"><a href="javascript:;"><i class="fa fa-icon "></i>restart kernel and clear output  <div title="jupyter-notebook:restart-kernel-and-clear-output" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="53"><a href="javascript:;"><i class="fa fa-icon "></i>restart kernel and run all cells  <div title="jupyter-notebook:restart-kernel-and-run-all-cells" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="54"><a href="javascript:;"><i class="fa fa-icon "></i>run all cells  <div title="jupyter-notebook:run-all-cells" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="55"><a href="javascript:;"><i class="fa fa-icon "></i>run all cells above  <div title="jupyter-notebook:run-all-cells-above" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="56"><a href="javascript:;"><i class="fa fa-icon "></i>run all cells below  <div title="jupyter-notebook:run-all-cells-below" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="57"><a href="javascript:;"><i class="fa fa-icon "></i>run cell and insert below  <div title="jupyter-notebook:run-cell-and-insert-below" class="pull-right command-shortcut"><kbd>Alt-Enter</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="58"><a href="javascript:;"><i class="fa fa-icon fa-step-forward"></i>run cell and select next  <div title="jupyter-notebook:run-cell-and-select-next" class="pull-right command-shortcut"><kbd>Shift-Enter</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="59"><a href="javascript:;"><i class="fa fa-icon "></i>run selected cells  <div title="jupyter-notebook:run-cell" class="pull-right command-shortcut"><kbd>Ctrl-Enter</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="60"><a href="javascript:;"><i class="fa fa-icon fa-save"></i>save notebook  <div title="jupyter-notebook:save-notebook" class="pull-right command-shortcut"><kbd>Ctrl-S</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="61"><a href="javascript:;"><i class="fa fa-icon "></i>scroll cell center  <div title="jupyter-notebook:scroll-cell-center" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="62"><a href="javascript:;"><i class="fa fa-icon "></i>scroll cell top  <div title="jupyter-notebook:scroll-cell-top" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="63"><a href="javascript:;"><i class="fa fa-icon "></i>scroll notebook down  <div title="jupyter-notebook:scroll-notebook-down" class="pull-right command-shortcut"><kbd>Space</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="64"><a href="javascript:;"><i class="fa fa-icon "></i>scroll notebook up  <div title="jupyter-notebook:scroll-notebook-up" class="pull-right command-shortcut"><kbd>Shift-Space</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="65"><a href="javascript:;"><i class="fa fa-icon "></i>select all  <div title="jupyter-notebook:select-all" class="pull-right command-shortcut"><kbd>Ctrl-A</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="66"><a href="javascript:;"><i class="fa fa-icon "></i>select next cell  <div title="jupyter-notebook:select-next-cell" class="pull-right command-shortcut"><kbd>Down</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="67"><a href="javascript:;"><i class="fa fa-icon "></i>select previous cell  <div title="jupyter-notebook:select-previous-cell" class="pull-right command-shortcut"><kbd>Up</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="68"><a href="javascript:;"><i class="fa fa-icon "></i>show all line numbers  <div title="jupyter-notebook:show-all-line-numbers" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="69"><a href="javascript:;"><i class="fa fa-icon fa-keyboard-o"></i>show command pallette  <div title="jupyter-notebook:show-command-palette" class="pull-right command-shortcut"><kbd>Ctrl-Shift-P</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="70"><a href="javascript:;"><i class="fa fa-icon "></i>show keyboard shortcuts  <div title="jupyter-notebook:show-keyboard-shortcuts" class="pull-right command-shortcut"><kbd>H</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="71"><a href="javascript:;"><i class="fa fa-icon "></i>show menubar  <div title="jupyter-notebook:show-menubar" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="72"><a href="javascript:;"><i class="fa fa-icon "></i>show the header  <div title="jupyter-notebook:show-header" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="73"><a href="javascript:;"><i class="fa fa-icon "></i>show the toolbar  <div title="jupyter-notebook:show-toolbar" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="74"><a href="javascript:;"><i class="fa fa-icon "></i>shutdown kernel  <div title="jupyter-notebook:shutdown-kernel" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="75"><a href="javascript:;"><i class="fa fa-icon "></i>shutdown kernel and close window  <div title="jupyter-notebook:close-and-halt" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="76"><a href="javascript:;"><i class="fa fa-icon "></i>split cell at cursor  <div title="jupyter-notebook:split-cell-at-cursor" class="pull-right edit-shortcut"><kbd>Ctrl-Shift-Minus</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="77"><a href="javascript:;"><i class="fa fa-icon "></i>toggle all cells output collapsed  <div title="jupyter-notebook:toggle-all-cells-output-collapsed" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="78"><a href="javascript:;"><i class="fa fa-icon "></i>toggle all cells output scrolled  <div title="jupyter-notebook:toggle-all-cells-output-scrolled" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="79"><a href="javascript:;"><i class="fa fa-icon fa-list-ol"></i>toggle all line numbers  <div title="jupyter-notebook:toggle-all-line-numbers" class="pull-right command-shortcut"><kbd>Shift-L</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="80"><a href="javascript:;"><i class="fa fa-icon "></i>toggle cell output  <div title="jupyter-notebook:toggle-cell-output-collapsed" class="pull-right command-shortcut"><kbd>O</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="81"><a href="javascript:;"><i class="fa fa-icon "></i>toggle cell scrolling  <div title="jupyter-notebook:toggle-cell-output-scrolled" class="pull-right command-shortcut"><kbd>Shift-O</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="82"><a href="javascript:;"><i class="fa fa-icon "></i>toggle header  <div title="jupyter-notebook:toggle-header" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="83"><a href="javascript:;"><i class="fa fa-icon "></i>toggle line numbers  <div title="jupyter-notebook:toggle-cell-line-numbers" class="pull-right command-shortcut"><kbd>L</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="84"><a href="javascript:;"><i class="fa fa-icon "></i>toggle menubar  <div title="jupyter-notebook:toggle-menubar" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="85"><a href="javascript:;"><i class="fa fa-icon "></i>toggle rtl layout  <div title="jupyter-notebook:toggle-rtl-layout" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="86"><a href="javascript:;"><i class="fa fa-icon "></i>toggle toolbar  <div title="jupyter-notebook:toggle-toolbar" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="87"><a href="javascript:;"><i class="fa fa-icon "></i>trust notebook  <div title="jupyter-notebook:trust-notebook" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="88"><a href="javascript:;"><i class="fa fa-icon "></i>undo cell deletion  <div title="jupyter-notebook:undo-cell-deletion" class="pull-right command-shortcut"><kbd>Z</kbd></div></a></li><li class="typeahead__group" data-search-group="widgets"><a href="javascript:;" tabindex="-1">widgets command group</a></li><li class="typeahead__item typeahead__group-widgets" data-group="widgets" data-index="89"><a href="javascript:;"><i class="fa fa-icon fa-sliders"></i>embed interactive widgets  <div title="widgets:embed-interactive-widgets" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-widgets" data-group="widgets" data-index="90"><a href="javascript:;"><i class="fa fa-icon fa-truck"></i>save clear widgets  <div title="widgets:save-clear-widgets" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-widgets" data-group="widgets" data-index="91"><a href="javascript:;"><i class="fa fa-icon fa-sliders"></i>save widget state  <div title="widgets:save-widget-state" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-widgets" data-group="widgets" data-index="92"><a href="javascript:;"><i class="fa fa-icon fa-truck"></i>save with widgets  <div title="widgets:save-with-widgets" class="pull-right no-shortcut"></div></a></li></ul></div></div></form></div></div></div></div><div class="modal cmd-palette" style="display: none;"><div class="modal-dialog"><div class="modal-content"><div class="modal-body"><form><div class="typeahead__container"><div class="typeahead__field"><span class="typeahead__query" style="position: relative;"><span class="typeahead__cancel-button">??</span><input type="search"><input type="search" readonly="readonly" unselectable="on" aria-hidden="true" tabindex="-1" class="typeahead__hint" style="border-color: transparent; position: absolute; top: 0px; display: inline; z-index: -1; float: none; color: rgb(192, 192, 192); box-shadow: none; cursor: default; user-select: none;"></span><span class="typeahead__button"><button type="submit"><span class="typeahead__search-icon"></span></button></span></div><div class="typeahead__result"><ul class="typeahead__list"><li class="typeahead__group" data-search-group="jupyter-notebook"><a href="javascript:;" tabindex="-1">jupyter-notebook command group</a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="0"><a href="javascript:;"><i class="fa fa-icon "></i>automatically indent selection  <div title="jupyter-notebook:auto-indent" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="1"><a href="javascript:;"><i class="fa fa-icon "></i>change cell to code  <div title="jupyter-notebook:change-cell-to-code" class="pull-right command-shortcut"><kbd>Y</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="2"><a href="javascript:;"><i class="fa fa-icon "></i>change cell to heading 1  <div title="jupyter-notebook:change-cell-to-heading-1" class="pull-right command-shortcut"><kbd>1</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="3"><a href="javascript:;"><i class="fa fa-icon "></i>change cell to heading 2  <div title="jupyter-notebook:change-cell-to-heading-2" class="pull-right command-shortcut"><kbd>2</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="4"><a href="javascript:;"><i class="fa fa-icon "></i>change cell to heading 3  <div title="jupyter-notebook:change-cell-to-heading-3" class="pull-right command-shortcut"><kbd>3</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="5"><a href="javascript:;"><i class="fa fa-icon "></i>change cell to heading 4  <div title="jupyter-notebook:change-cell-to-heading-4" class="pull-right command-shortcut"><kbd>4</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="6"><a href="javascript:;"><i class="fa fa-icon "></i>change cell to heading 5  <div title="jupyter-notebook:change-cell-to-heading-5" class="pull-right command-shortcut"><kbd>5</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="7"><a href="javascript:;"><i class="fa fa-icon "></i>change cell to heading 6  <div title="jupyter-notebook:change-cell-to-heading-6" class="pull-right command-shortcut"><kbd>6</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="8"><a href="javascript:;"><i class="fa fa-icon "></i>change cell to markdown  <div title="jupyter-notebook:change-cell-to-markdown" class="pull-right command-shortcut"><kbd>M</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="9"><a href="javascript:;"><i class="fa fa-icon "></i>change cell to raw  <div title="jupyter-notebook:change-cell-to-raw" class="pull-right command-shortcut"><kbd>R</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="10"><a href="javascript:;"><i class="fa fa-icon "></i>clear all cells output  <div title="jupyter-notebook:clear-all-cells-output" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="11"><a href="javascript:;"><i class="fa fa-icon "></i>clear cell output  <div title="jupyter-notebook:clear-cell-output" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="12"><a href="javascript:;"><i class="fa fa-icon "></i>close the pager  <div title="jupyter-notebook:close-pager" class="pull-right command-shortcut"><kbd>Esc</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="13"><a href="javascript:;"><i class="fa fa-icon fa-repeat"></i>confirm restart kernel  <div title="jupyter-notebook:confirm-restart-kernel" class="pull-right command-shortcut"><kbd>0</kbd>,<kbd>0</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="14"><a href="javascript:;"><i class="fa fa-icon "></i>confirm restart kernel and clear output  <div title="jupyter-notebook:confirm-restart-kernel-and-clear-output" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="15"><a href="javascript:;"><i class="fa fa-icon fa-forward"></i>confirm restart kernel and run all cells  <div title="jupyter-notebook:confirm-restart-kernel-and-run-all-cells" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="16"><a href="javascript:;"><i class="fa fa-icon fa-repeat"></i>confirm shutdown kernel  <div title="jupyter-notebook:confirm-shutdown-kernel" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="17"><a href="javascript:;"><i class="fa fa-icon "></i>copy cell attachments  <div title="jupyter-notebook:copy-cell-attachments" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="18"><a href="javascript:;"><i class="fa fa-icon fa-copy"></i>copy selected cells  <div title="jupyter-notebook:copy-cell" class="pull-right command-shortcut"><kbd>C</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="19"><a href="javascript:;"><i class="fa fa-icon "></i>cut cell attachments  <div title="jupyter-notebook:cut-cell-attachments" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="20"><a href="javascript:;"><i class="fa fa-icon fa-cut"></i>cut selected cells  <div title="jupyter-notebook:cut-cell" class="pull-right command-shortcut"><kbd>X</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="21"><a href="javascript:;"><i class="fa fa-icon "></i>delete cells  <div title="jupyter-notebook:delete-cell" class="pull-right command-shortcut"><kbd>D</kbd>,<kbd>D</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="22"><a href="javascript:;"><i class="fa fa-icon "></i>duplicate notebook  <div title="jupyter-notebook:duplicate-notebook" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="23"><a href="javascript:;"><i class="fa fa-icon "></i>edit command mode keyboard shortcuts  <div title="jupyter-notebook:edit-command-mode-keyboard-shortcuts" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="24"><a href="javascript:;"><i class="fa fa-icon "></i>enter command mode  <div title="jupyter-notebook:enter-command-mode" class="pull-right edit-shortcut"><kbd>Esc</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="25"><a href="javascript:;"><i class="fa fa-icon "></i>enter edit mode  <div title="jupyter-notebook:enter-edit-mode" class="pull-right command-shortcut"><kbd>Enter</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="26"><a href="javascript:;"><i class="fa fa-icon "></i>extend selection above  <div title="jupyter-notebook:extend-selection-above" class="pull-right command-shortcut"><kbd>Shift-K</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="27"><a href="javascript:;"><i class="fa fa-icon "></i>extend selection below  <div title="jupyter-notebook:extend-selection-below" class="pull-right command-shortcut"><kbd>Shift-J</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="28"><a href="javascript:;"><i class="fa fa-icon "></i>find and replace  <div title="jupyter-notebook:find-and-replace" class="pull-right command-shortcut"><kbd>F</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="29"><a href="javascript:;"><i class="fa fa-icon "></i>hide all line numbers  <div title="jupyter-notebook:hide-all-line-numbers" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="30"><a href="javascript:;"><i class="fa fa-icon "></i>hide menubar  <div title="jupyter-notebook:hide-menubar" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="31"><a href="javascript:;"><i class="fa fa-icon "></i>hide the header  <div title="jupyter-notebook:hide-header" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="32"><a href="javascript:;"><i class="fa fa-icon "></i>hide the toolbar  <div title="jupyter-notebook:hide-toolbar" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="33"><a href="javascript:;"><i class="fa fa-icon "></i>ignore  <div title="jupyter-notebook:ignore" class="pull-right command-shortcut"><kbd>Shift</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="34"><a href="javascript:;"><i class="fa fa-icon "></i>insert cell above  <div title="jupyter-notebook:insert-cell-above" class="pull-right command-shortcut"><kbd>A</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="35"><a href="javascript:;"><i class="fa fa-icon fa-plus"></i>insert cell below  <div title="jupyter-notebook:insert-cell-below" class="pull-right command-shortcut"><kbd>B</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="36"><a href="javascript:;"><i class="fa fa-icon "></i>insert image  <div title="jupyter-notebook:insert-image" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="37"><a href="javascript:;"><i class="fa fa-icon fa-stop"></i>interrupt the kernel  <div title="jupyter-notebook:interrupt-kernel" class="pull-right command-shortcut"><kbd>I</kbd>,<kbd>I</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="38"><a href="javascript:;"><i class="fa fa-icon "></i>merge cell with next cell  <div title="jupyter-notebook:merge-cell-with-next-cell" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="39"><a href="javascript:;"><i class="fa fa-icon "></i>merge cell with previous cell  <div title="jupyter-notebook:merge-cell-with-previous-cell" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="40"><a href="javascript:;"><i class="fa fa-icon "></i>merge cells  <div title="jupyter-notebook:merge-cells" class="pull-right command-shortcut"><kbd>Shift-M</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="41"><a href="javascript:;"><i class="fa fa-icon "></i>merge selected cells  <div title="jupyter-notebook:merge-selected-cells" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="42"><a href="javascript:;"><i class="fa fa-icon fa-arrow-down"></i>move cells down  <div title="jupyter-notebook:move-cell-down" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="43"><a href="javascript:;"><i class="fa fa-icon fa-arrow-up"></i>move cells up  <div title="jupyter-notebook:move-cell-up" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="44"><a href="javascript:;"><i class="fa fa-icon "></i>move cursor down  <div title="jupyter-notebook:move-cursor-down" class="pull-right edit-shortcut"><kbd>Down</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="45"><a href="javascript:;"><i class="fa fa-icon "></i>move cursor up  <div title="jupyter-notebook:move-cursor-up" class="pull-right edit-shortcut"><kbd>Up</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="46"><a href="javascript:;"><i class="fa fa-icon "></i>paste cell attachments  <div title="jupyter-notebook:paste-cell-attachments" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="47"><a href="javascript:;"><i class="fa fa-icon "></i>paste cell replace  <div title="jupyter-notebook:paste-cell-replace" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="48"><a href="javascript:;"><i class="fa fa-icon "></i>paste cells above  <div title="jupyter-notebook:paste-cell-above" class="pull-right command-shortcut"><kbd>Shift-V</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="49"><a href="javascript:;"><i class="fa fa-icon fa-paste"></i>paste cells below  <div title="jupyter-notebook:paste-cell-below" class="pull-right command-shortcut"><kbd>V</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="50"><a href="javascript:;"><i class="fa fa-icon "></i>rename notebook  <div title="jupyter-notebook:rename-notebook" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="51"><a href="javascript:;"><i class="fa fa-icon "></i>restart kernel  <div title="jupyter-notebook:restart-kernel" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="52"><a href="javascript:;"><i class="fa fa-icon "></i>restart kernel and clear output  <div title="jupyter-notebook:restart-kernel-and-clear-output" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="53"><a href="javascript:;"><i class="fa fa-icon "></i>restart kernel and run all cells  <div title="jupyter-notebook:restart-kernel-and-run-all-cells" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="54"><a href="javascript:;"><i class="fa fa-icon "></i>run all cells  <div title="jupyter-notebook:run-all-cells" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="55"><a href="javascript:;"><i class="fa fa-icon "></i>run all cells above  <div title="jupyter-notebook:run-all-cells-above" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="56"><a href="javascript:;"><i class="fa fa-icon "></i>run all cells below  <div title="jupyter-notebook:run-all-cells-below" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="57"><a href="javascript:;"><i class="fa fa-icon "></i>run cell and insert below  <div title="jupyter-notebook:run-cell-and-insert-below" class="pull-right command-shortcut"><kbd>Alt-Enter</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="58"><a href="javascript:;"><i class="fa fa-icon fa-step-forward"></i>run cell and select next  <div title="jupyter-notebook:run-cell-and-select-next" class="pull-right command-shortcut"><kbd>Shift-Enter</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="59"><a href="javascript:;"><i class="fa fa-icon "></i>run selected cells  <div title="jupyter-notebook:run-cell" class="pull-right command-shortcut"><kbd>Ctrl-Enter</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="60"><a href="javascript:;"><i class="fa fa-icon fa-save"></i>save notebook  <div title="jupyter-notebook:save-notebook" class="pull-right command-shortcut"><kbd>Ctrl-S</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="61"><a href="javascript:;"><i class="fa fa-icon "></i>scroll cell center  <div title="jupyter-notebook:scroll-cell-center" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="62"><a href="javascript:;"><i class="fa fa-icon "></i>scroll cell top  <div title="jupyter-notebook:scroll-cell-top" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="63"><a href="javascript:;"><i class="fa fa-icon "></i>scroll notebook down  <div title="jupyter-notebook:scroll-notebook-down" class="pull-right command-shortcut"><kbd>Space</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="64"><a href="javascript:;"><i class="fa fa-icon "></i>scroll notebook up  <div title="jupyter-notebook:scroll-notebook-up" class="pull-right command-shortcut"><kbd>Shift-Space</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="65"><a href="javascript:;"><i class="fa fa-icon "></i>select all  <div title="jupyter-notebook:select-all" class="pull-right command-shortcut"><kbd>Ctrl-A</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="66"><a href="javascript:;"><i class="fa fa-icon "></i>select next cell  <div title="jupyter-notebook:select-next-cell" class="pull-right command-shortcut"><kbd>Down</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="67"><a href="javascript:;"><i class="fa fa-icon "></i>select previous cell  <div title="jupyter-notebook:select-previous-cell" class="pull-right command-shortcut"><kbd>Up</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="68"><a href="javascript:;"><i class="fa fa-icon "></i>show all line numbers  <div title="jupyter-notebook:show-all-line-numbers" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="69"><a href="javascript:;"><i class="fa fa-icon fa-keyboard-o"></i>show command pallette  <div title="jupyter-notebook:show-command-palette" class="pull-right command-shortcut"><kbd>Ctrl-Shift-P</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="70"><a href="javascript:;"><i class="fa fa-icon "></i>show keyboard shortcuts  <div title="jupyter-notebook:show-keyboard-shortcuts" class="pull-right command-shortcut"><kbd>H</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="71"><a href="javascript:;"><i class="fa fa-icon "></i>show menubar  <div title="jupyter-notebook:show-menubar" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="72"><a href="javascript:;"><i class="fa fa-icon "></i>show the header  <div title="jupyter-notebook:show-header" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="73"><a href="javascript:;"><i class="fa fa-icon "></i>show the toolbar  <div title="jupyter-notebook:show-toolbar" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="74"><a href="javascript:;"><i class="fa fa-icon "></i>shutdown kernel  <div title="jupyter-notebook:shutdown-kernel" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="75"><a href="javascript:;"><i class="fa fa-icon "></i>shutdown kernel and close window  <div title="jupyter-notebook:close-and-halt" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="76"><a href="javascript:;"><i class="fa fa-icon "></i>split cell at cursor  <div title="jupyter-notebook:split-cell-at-cursor" class="pull-right edit-shortcut"><kbd>Ctrl-Shift-Minus</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="77"><a href="javascript:;"><i class="fa fa-icon "></i>toggle all cells output collapsed  <div title="jupyter-notebook:toggle-all-cells-output-collapsed" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="78"><a href="javascript:;"><i class="fa fa-icon "></i>toggle all cells output scrolled  <div title="jupyter-notebook:toggle-all-cells-output-scrolled" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="79"><a href="javascript:;"><i class="fa fa-icon fa-list-ol"></i>toggle all line numbers  <div title="jupyter-notebook:toggle-all-line-numbers" class="pull-right command-shortcut"><kbd>Shift-L</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="80"><a href="javascript:;"><i class="fa fa-icon "></i>toggle cell output  <div title="jupyter-notebook:toggle-cell-output-collapsed" class="pull-right command-shortcut"><kbd>O</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="81"><a href="javascript:;"><i class="fa fa-icon "></i>toggle cell scrolling  <div title="jupyter-notebook:toggle-cell-output-scrolled" class="pull-right command-shortcut"><kbd>Shift-O</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="82"><a href="javascript:;"><i class="fa fa-icon "></i>toggle header  <div title="jupyter-notebook:toggle-header" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="83"><a href="javascript:;"><i class="fa fa-icon "></i>toggle line numbers  <div title="jupyter-notebook:toggle-cell-line-numbers" class="pull-right command-shortcut"><kbd>L</kbd></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="84"><a href="javascript:;"><i class="fa fa-icon "></i>toggle menubar  <div title="jupyter-notebook:toggle-menubar" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="85"><a href="javascript:;"><i class="fa fa-icon "></i>toggle rtl layout  <div title="jupyter-notebook:toggle-rtl-layout" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="86"><a href="javascript:;"><i class="fa fa-icon "></i>toggle toolbar  <div title="jupyter-notebook:toggle-toolbar" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="87"><a href="javascript:;"><i class="fa fa-icon "></i>trust notebook  <div title="jupyter-notebook:trust-notebook" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-jupyter-notebook" data-group="jupyter-notebook" data-index="88"><a href="javascript:;"><i class="fa fa-icon "></i>undo cell deletion  <div title="jupyter-notebook:undo-cell-deletion" class="pull-right command-shortcut"><kbd>Z</kbd></div></a></li><li class="typeahead__group" data-search-group="widgets"><a href="javascript:;" tabindex="-1">widgets command group</a></li><li class="typeahead__item typeahead__group-widgets" data-group="widgets" data-index="89"><a href="javascript:;"><i class="fa fa-icon fa-sliders"></i>embed interactive widgets  <div title="widgets:embed-interactive-widgets" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-widgets" data-group="widgets" data-index="90"><a href="javascript:;"><i class="fa fa-icon fa-truck"></i>save clear widgets  <div title="widgets:save-clear-widgets" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-widgets" data-group="widgets" data-index="91"><a href="javascript:;"><i class="fa fa-icon fa-sliders"></i>save widget state  <div title="widgets:save-widget-state" class="pull-right no-shortcut"></div></a></li><li class="typeahead__item typeahead__group-widgets" data-group="widgets" data-index="92"><a href="javascript:;"><i class="fa fa-icon fa-truck"></i>save with widgets  <div title="widgets:save-with-widgets" class="pull-right no-shortcut"></div></a></li></ul></div></div></form></div></div></div></div></body></html>