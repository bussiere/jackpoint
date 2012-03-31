// Wrapper must be set before anything else or you can see the windows jump on load
$('#wrapper').css({width: screen.width, height: window.innerHeight});

$(document).ready(function() {

	initializePage();

});

function initializePage() {
	switch ( GLOBAL_PAGE ) {
		case 'INDEX':
			setupLogin();
			break;
		case 'FAQ':
			setupFAQ();
			break;
	}
}



/*================================================================================================*/
/* Login Page */

function setupLogin() {
	// Draw Logo
	//DRAW.logo($('#logo'));

	// IE does not support HTML5 placeholders, use manual input values
	var $inputs = $('#login_inputs input.log-input').add('#invite_input_wrapper input');
	checkPlaceholders($inputs);
	
	// Set window drag
	$('#login_wrapper').draggable({cancel: '#login_window, #login_faq'});
	$('#copyright_wrapper').draggable({cancel: '#copyright_window'});
	$('#invite_wrapper').draggable({cancel: '#invite_window'});
	
	// Set drag z-index manager
	$('#wrapper div.jp-wrapper').draggable('option', 'stack', '#wrapper div.jp-wrapper');
	
	// Show the dialog when the user click the invitation link
	$('#invitation_link').click(function(e) {
		e.preventDefault();
		$('#invite_wrapper').show();
		
		// only draw rabbit once
		//if ( $('#invite_rabbit').html() == '' ) {
			//DRAW.rabbit($('#invite_rabbit'));
		//}
	});
	
	// Hide the dialog
	$('#invite_cancel').click(function() {
		// Clear values before hiding
		$('#invite_input_wrapper input[type=text]').val('');
		$('#invite_wrapper').hide();
	});
	
	//$('#login_window').animate({'clip': 'rect(0px, 657px, 257px, 0px)'}, 750);
}





/*================================================================================================*/
/* FAQ */

function setupFAQ() {
	// Set scrollbar for faq
	$('#faq_wrapper').jScrollPane({"verticalGutter": 10, "hijackInternalLinks": true});
	
	// Fix weird bug with scrollbar
	var x=$('#faq_wrapper').data('jsp');
	x.getContentPane().height(x.getContentHeight());
	
	// Check placeholders
	var $inputs = $('#qlogin_inputs input');
	checkPlaceholders($inputs);
	
	// Set ajax listener for login input
	$('#qlogin_btn').click(function() {
		// For testing
		var text = '';
		
		$inputs.each(function() {
			text += $(this).val();
		});
		
		alert(text);
	});
	
	// Scale font on buttons
	//console.log($('#faq_navigation .jp-window-button p').height());
	//var $btn = $('#faq_navigation .jp-window-button p');
	//$btn.css({'font-size': $btn.height()*0.35});
}



/*================================================================================================*/
/* Draw Object */
/*
var DRAW = {
	rabbit: function(container) {
		var offset = container.offset();
		var h = container.height();
		var w = container.width();
		
		var paper = Raphael(offset.left, offset.top, w, h);
		
		var path = paper.path('M20,60v-5h5v-5h5v-5h5v-5h10v-10h5v-15h5v-5h15v5h10v25h-5v5h-10v10h5v15h15v5h30v5h15v5h5v5h5v5h5v5h5v5h5v5h5v10h5v30h-5v5h-5v5h5v15h-20v-5h-15v5h-60v-15h25v-5h-5v-5h-5v-5h-5v-5h-5v15h-15v5h-5v5h-25v-5h10v-5h5v-10h5v-10h-5v-5h-5v-5h-5v-20h-5v-20h-5v-5h-5v-5h-5v-10h5m20,0h10v-10h-10v10m-20,0v-5h5')
		.attr({stroke: 'green', 'stroke-width': 2, fill: '#fff', 'fill-opacity': 0.5})
		.transform('s-1,1t-25,0');
		
		container.append($(path.node).parent().css({top:0,left:0}));
	},
	
	logo: function(container) {
		// Setup paper viewport
		var h 		= container.height();
		var paper 	= Raphael(container, container.width(), h);
		
		// Draw logo and get scale ratio
		var path 	= paper.path('M7,7L27,7V18H19V28H7V24H15V18H7V14H15M19,14H23V11H19V14M15,14V11H7V7');
		var bb 		= path.getBBox(false);
		var ratio 	= h / bb.height;
		
		// Set scale/transform/color and set hover/click listener
		path.attr({fill:'#00ff32', stroke:'none', 'fill-opacity':0.5})
		.transform('T-7,-7S'+ratio+','+ratio+'t'+bb.width*0.55+','+bb.height*0.45);
		
		// Append the svg drawing to the parent element
		container.append($(path.node).parent().css({top:0,left:0}));
		
		return path;
	}
};
*/



/*================================================================================================*/
/* Useful functions */

function checkPlaceholders($elements) {
	test = document.createElement('input');

	if(!('placeholder' in test)) {
		var inputs = $elements;
		
		inputs.each(function() {
			$(this).val($(this).attr('placeholder'));
		})
		.focus(function() {
			if ( $(this).val() == $(this).attr('placeholder') ) {
				$(this).val('');
			}
		})
		.blur(function() {
			if ( $(this).val() == '' ) {
				$(this).val($(this).attr('placeholder'));
			}
		});
	}
}



/*================================================================================================*/
/* Extra Plugin + Object */

/*
 * jQuery css clip animation support -- Jim Palmer
 * version 0.1.2
 * idea spawned from jquery.color.js by John Resig
 * Released under the MIT license.
 */
 /*
(function(jQuery){
	jQuery.fx.step.clip = function(fx){
		if ( fx.state == 0 ) {
			var cRE = /rect\(([0-9]{1,})(px|em)[,]? ([0-9]{1,})(px|em)[,]? ([0-9]{1,})(px|em)[,]? ([0-9]{1,})(px|em)\)/;
			fx.start = cRE.exec( fx.elem.style.clip.replace(/,/g, '') );
			fx.end = cRE.exec( fx.end.replace(/,/g, '') );
		}
		var sarr = new Array(), earr = new Array(), spos = fx.start.length, epos = fx.end.length,
			emOffset = fx.start[ss+1] == 'em' ? ( parseInt($(fx.elem).css('fontSize')) * 1.333 * parseInt(fx.start[ss]) ) : 1;
		for ( var ss = 1; ss < spos; ss+=2 ) { sarr.push( parseInt( emOffset * fx.start[ss] ) ); }
		for ( var es = 1; es < epos; es+=2 ) { earr.push( parseInt( emOffset * fx.end[es] ) ); }
		fx.elem.style.clip = 'rect(' + 
			parseInt( ( fx.pos * ( earr[0] - sarr[0] ) ) + sarr[0] ) + 'px ' + 
			parseInt( ( fx.pos * ( earr[1] - sarr[1] ) ) + sarr[1] ) + 'px ' +
			parseInt( ( fx.pos * ( earr[2] - sarr[2] ) ) + sarr[2] ) + 'px ' + 
			parseInt( ( fx.pos * ( earr[3] - sarr[3] ) ) + sarr[3] ) + 'px)';
	}
})(jQuery);
*/