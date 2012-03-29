// Wrapper must be set before anything else or you can see the windows jump on load
$('#wrapper').css({width: screen.width, height: window.innerHeight});

$(document).ready(function() {

	setupLogin();

});

function setupLogin() {
	// draw logo
	var Logo = drawsvg($('#logo'));
	
	// IE does not support HTML5 placeholders, use manual input values
	checkPlaceholders();
	
	// Set drag and animation
	//$('#login_window').animate({'clip': 'rect(0px, 657px, 257px, 0px)'}, 750);
	$('#login_wrapper').draggable({cancel: '#login_window, #login_faq'});
	$('#copyright_wrapper').draggable({cancel: '#copyright_window'});
}

function checkPlaceholders() {
	test = document.createElement('input');

	if(!('placeholder' in test)) {
		var inputs = $('#login_inputs input.log-input');
		
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

function drawsvg(container) {
	//var offset = container.offset();
	//var w = container.width();
	
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
	/*.hover(function() {
		this.attr('stroke', '#00ff32');
	}, function() {
		this.attr('stroke', 'none');
	})*///;
	//translate(-7,-7).scale(ratio,ratio).translate(bb.width*0.55, bb.height*0.45);
	
	// Append the svg drawing to the parent element
	container.append($(path.node).parent().css({top:0,left:0}));
	
	return path;
}



/*================================================================================================*/
/* Extra Plugin + Object */

/*
 * jQuery css clip animation support -- Jim Palmer
 * version 0.1.2
 * idea spawned from jquery.color.js by John Resig
 * Released under the MIT license.
 */
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