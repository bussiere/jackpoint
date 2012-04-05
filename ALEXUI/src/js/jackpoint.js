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
			
		case 'HELP_1':
			setupHelp();
			break;
		
		case 'PLACE_1':
			setupPlaces();
			break;
	}
}

/*================================================================================================*/
/* Always Run */

function upkeep() {
	// Scale svg logo
	var a = ($('#jackpoint_banner_wrapper').height() * 0.75) / 27;
	
	$('#logosvg path').attr('transform', 'matrix('+a+',0,0,'+a+',0,0)').click(function() {
		window.location = 'index.html';
	});
	
	var b = $('#user_image');
	
	b.width(b.height());
}



/*================================================================================================*/
/* Login Page */

function setupLogin() {
	// IE does not support HTML5 placeholders, use manual input values
	var $inputs = $('#login_inputs input[type=text]').add('#login_inputs input[type=password]').add('#invite_input_wrapper input');
	checkPlaceholders($inputs);
	
	// Set window drag
	$('#login_wrapper').draggable({cancel: '#login_window, #login_faq'});
	$('#copyright_wrapper').draggable({cancel: '#copyright_window'});
	$('#invite_wrapper').draggable({cancel: '#invite_window'});
	$('#youtube_wrapper').draggable({cancel: '#youtube_control'});
	
	// Set drag z-index manager
	$('#wrapper div.jp-wrapper').draggable('option', 'stack', '#wrapper div.jp-wrapper');
	
	DRAW.banner($('#banner_wrapper'));
	
	// Show the dialog when the user click the invitation link
	$('#invitation_link').click(function(e) {
		e.preventDefault();
		$('#invite_wrapper').show('blind');
	});
	
	// Hide the dialog
	$('#invite_cancel').click(function() {
		// Clear values before hiding
		$('#invite_input_wrapper input[type=text]').val('');
		$('#invite_wrapper').hide();
	});
}



/*================================================================================================*/
/* FAQ */

function setupFAQ() {
	// Fix weird bug with scrollbar
	$('#faq_window section.faq-section').each(function() {
		$(this).height($(this).height());
	});

	// Set scrollbar for faq
	$('#faq_wrapper').jScrollPane({"verticalGutter": 10, "hijackInternalLinks": true});

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
}



/*================================================================================================*/
/* Help Page */

function setupHelp() {
	upkeep();
	radioButtonEvent();
	
	// load first step
	help_description.load();
	
	// See below for the objects
	$('#skill_next_btn').click(function() {
		switch ( GLOBAL_PAGE ) {
		
			case 'HELP_1':
			if ( help_description.save() ) help_min.load();
			break;
			
			case 'HELP_2':
			if ( help_min.save() ) help_skills.load();
			break;
			
			case 'HELP_3':
			if ( help_skills.save() ) help_object.load();
			break;
			
			case 'HELP_4':
			if ( help_object.save() ) help_confirm.load();
			break;
			
			case 'HELP_5':
			
				// PUT DATA INTO DATABASE OR SOMETHING
				console.log(help_description);
				console.log(help_min);
				console.log(help_skills);
				console.log(help_object);
				
			break;
		}
	});
	
	$('#skill_back_btn').click(function() {
		switch ( GLOBAL_PAGE ) {
			case 'HELP_2':
			help_description.load();
			break;
			
			case 'HELP_3':
			help_min.load();
			break;
			
			case 'HELP_4':
			help_skills.load();
			break;
			
			case 'HELP_5':
			help_object.load();
			break;
		}
	});
}

var help_description = {
	description: 	'',
	tag: 			'',
	
	load: function() {
		GLOBAL_PAGE = 'HELP_1';
		changeIndicator(0);
		
		$('#skill_window').load('include/help_request_1.html', function() {
			help_description.recall();

			$('#skill_percentage').html('<p>0%</p>');
		});
	},
	
	save: function() {
		// save work
		var a 							= $('#skill_description textarea');
		help_description.description 	= a.eq(0).val();
		help_description.tag 			= a.eq(1).val();
		
		// check values
		if ( help_description.description == '' || help_description.tag == '' ) {
			return false;
		}
		console.log(this);
		return true;
	},
	
	recall: function() {
		var a = $('#skill_description textarea');
		a.eq(0).val(help_description.description);
		a.eq(1).val(help_description.tag);
	}
};

var help_min = {
	Force: 		'',
	Logique: 	'',
	Volonte: 	'',
	Charisme: 	'',
	Apparence: 	'',
	Dexterite: 	'',
	
	save: function() {
		var a = $('#skill_content div.jp-radio-btn-selected');
		
		// check values
		if ( a.length != 6 ) return false;
		
		// save work
		this.Force 		= $.trim(a.eq(0).text());
		this.Logique 	= $.trim(a.eq(1).text());
		this.Volonte 	= $.trim(a.eq(2).text());
		this.Charisme 	= $.trim(a.eq(3).text());
		this.Apparence 	= $.trim(a.eq(4).text());
		this.Dexterite 	= $.trim(a.eq(5).text());
		
		//console.log(this);
		
		return true;
	},
	
	recall: function() {
		// Load previous data
		if ( this.Force != '' ) 	$('#force_group div.jp-radio-btn').eq(this.Force).addClass('jp-radio-btn-selected');
		if ( this.Logique != '' ) 	$('#logique_group div.jp-radio-btn').eq(this.Logique).addClass('jp-radio-btn-selected');
		if ( this.Volonte != '' ) 	$('#volonte_group div.jp-radio-btn').eq(this.Volonte).addClass('jp-radio-btn-selected');
		if ( this.Charisme != '' )	$('#charisme_group div.jp-radio-btn').eq(this.Charisme).addClass('jp-radio-btn-selected');
		if ( this.Apparence != '' ) $('#apparence_group div.jp-radio-btn').eq(this.Apparence).addClass('jp-radio-btn-selected');
		if ( this.Dexterite != '' ) $('#dexterite_group div.jp-radio-btn').eq(this.Dexterite).addClass('jp-radio-btn-selected');
	},
	
	load: function(callback) {
		GLOBAL_PAGE = 'HELP_2';
		changeIndicator(1);
		
		$('#skill_window').load('include/help_request_2.html', function() {
			help_min.recall();

			$('#skill_percentage').html('<p>20%</p>');
			
			fixRadioCSS();
			
			if ( callback ) callback();
		});
	},
	
	getArray: function() {
		return new Array(this.Force, this.Logique, this.Volonte, this.Charisme, this.Apparence, this.Dexterite);
	}
};

var help_skills = {
	Technique: 		'',
	Mettalerrie: 	'',
	Forge: 			'',
	Physique: 		'',
	Sport:			'',
	Karate:			'',
	Sud:			'',
	Nord:			'',
	Capoeira:		'',
	Bengale:		'',
	Savoir:			'',
	Informatique:	'',
	Programmation:	'',
	Python:			'',
	Web2py:			'',
	Django:			'',
	Methode:		'',
	Uml:			'',
	Merise:			'',
	
	load: function(callback) {
		GLOBAL_PAGE = 'HELP_3';
		changeIndicator(2);
		
		$('#skill_window').load('include/help_request_3.html', function() {
			help_skills.recall();
		
			$('#skill_percentage').html('<p>40%</p>');
	
			fixRadioCSS();
			
			$('.skill_row').css({height: $('.skill_row:first').height()});
			$('#skill_row_wrapper').css({height: '80%'}).jScrollPane();
			
			if ( callback ) callback();
		});
	},
	
	save: function() {
		var a = $('#skill_content div.jp-radio-btn-selected');
		
		// check values
		if ( a.length != 19 ) {
			return false;
		}
		
		// save work
		this.Technique 		= $.trim(a.eq(0).text());
		this.Mettalerrie 	= $.trim(a.eq(1).text());
		this.Forge 			= $.trim(a.eq(2).text());
		this.Physique 		= $.trim(a.eq(3).text());
		this.Sport 			= $.trim(a.eq(4).text());
		this.Karate 		= $.trim(a.eq(5).text());
		this.Sud 			= $.trim(a.eq(6).text());
		this.Nord			= $.trim(a.eq(7).text());
		this.Capoeira 		= $.trim(a.eq(8).text());
		this.Bengale 		= $.trim(a.eq(9).text());
		this.Savoir 		= $.trim(a.eq(10).text());
		this.Informatique 	= $.trim(a.eq(11).text());
		this.Programmation 	= $.trim(a.eq(12).text());
		this.Python 		= $.trim(a.eq(13).text());
		this.Web2py 		= $.trim(a.eq(14).text());
		this.Django 		= $.trim(a.eq(15).text());
		this.Methode 		= $.trim(a.eq(16).text());
		this.Uml 			= $.trim(a.eq(17).text());
		this.Merise 		= $.trim(a.eq(18).text());
		
		//console.log(this);
		
		return true;
	},
	
	recall: function() {
		// Load previous data
		if ( this.Technique != '' ) 		$('#technique_group div.jp-radio-btn').eq(this.Technique).addClass('jp-radio-btn-selected');
		if ( this.Mettalerrie != '' ) 		$('#mettalerrie_group div.jp-radio-btn').eq(this.Mettalerrie).addClass('jp-radio-btn-selected');
		if ( this.Forge != '' ) 			$('#forge_group div.jp-radio-btn').eq(this.Forge).addClass('jp-radio-btn-selected');
		if ( this.Physique != '' )			$('#physique_group div.jp-radio-btn').eq(this.Physique).addClass('jp-radio-btn-selected');
		if ( this.Sport != '' ) 			$('#sport_group div.jp-radio-btn').eq(this.Sport).addClass('jp-radio-btn-selected');
		if ( this.Karate != '' ) 			$('#karate_group div.jp-radio-btn').eq(this.Karate).addClass('jp-radio-btn-selected');
		if ( this.Sud != '' ) 				$('#sud_group div.jp-radio-btn').eq(this.Sud).addClass('jp-radio-btn-selected');
		if ( this.Nord != '' ) 				$('#nord_group div.jp-radio-btn').eq(this.Nord).addClass('jp-radio-btn-selected');
		if ( this.Capoeira != '' ) 			$('#capoeira_group div.jp-radio-btn').eq(this.Capoeira).addClass('jp-radio-btn-selected');
		if ( this.Bengale != '' )			$('#bengale_group div.jp-radio-btn').eq(this.Bengale).addClass('jp-radio-btn-selected');
		if ( this.Savoir != '' )	 		$('#savoir_group div.jp-radio-btn').eq(this.Savoir).addClass('jp-radio-btn-selected');
		if ( this.Informatique != '' ) 		$('#informatique_group div.jp-radio-btn').eq(this.Informatique).addClass('jp-radio-btn-selected');
		if ( this.Programmation != '' ) 	$('#programmation_group div.jp-radio-btn').eq(this.Programmation).addClass('jp-radio-btn-selected');
		if ( this.Python != '' ) 			$('#python_group div.jp-radio-btn').eq(this.Python).addClass('jp-radio-btn-selected');
		if ( this.Web2py != '' ) 			$('#web2py_group div.jp-radio-btn').eq(this.Web2py).addClass('jp-radio-btn-selected');
		if ( this.Django != '' ) 			$('#django_group div.jp-radio-btn').eq(this.Django).addClass('jp-radio-btn-selected');
		if ( this.Methode != '' )			$('#methode_group div.jp-radio-btn').eq(this.Methode).addClass('jp-radio-btn-selected');
		if ( this.Uml != '' ) 				$('#uml_group div.jp-radio-btn').eq(this.Uml).addClass('jp-radio-btn-selected');
		if ( this.Merise != '' ) 			$('#merise_group div.jp-radio-btn').eq(this.Merise).addClass('jp-radio-btn-selected');
	},
	
	getArray: function() {
		return new Array( this.Technique, this.Mettalerrie, this.Forge, this.Physique, this.Sport, this.Karate, this.Sud, this.Nord, this.Capoeira,
		this.Bengale, this.Savoir, this.Informatique, this.Programmation, this.Python, this.Web2py, this.Django, this.Methode, this.Uml, this.Merise);
	}
};

var help_object = {
	plasma: '',
	coudre: '',
	voiture: '',
	
	load: function(callback) {
		GLOBAL_PAGE = 'HELP_4';
		changeIndicator(3);
		
		$('#skill_window').load('include/help_request_4.html', function() {
			help_object.recall();
		
			$('#skill_percentage').html('<p>60%</p>');
		});
		
		if ( callback ) callback();
	},
	
	save: function() {
		var a = $('#skill_objects input');
		
		if ( a.eq(0).is(':checked') ) this.plasma = true;
		if ( a.eq(1).is(':checked') ) this.coudre = true;
		if ( a.eq(2).is(':checked') ) this.voiture = true;
		
		//console.log(this);
		
		return true;
	},
	
	recall: function() {
		var a = $('#skill_objects input');
		
		if ( this.plasma )  a.eq(0).attr('checked', 'checked');
		if ( this.coudre )  a.eq(1).attr('checked', 'checked');
		if ( this.voiture ) a.eq(2).attr('checked', 'checked');
	}
};

var help_confirm = {

	load: function(callback) {
		GLOBAL_PAGE = 'HELP_5';
		changeIndicator(4);
		
		$('#skill_window').load('include/help_request_5.html', function() {
			$('#skill_percentage').html('<p>80%</p>');
			
			$('#descriptbox').html(help_description.description);
			$('#tagbox').html(help_description.tag);
			
			var label1 = new Array('Force: ', 'Logique: ', 'Volonte: ', 'Charisme: ', 'Apparence: ', 'Dexterite: ');
			var label2 = new Array('Technique: ', 'Metallerrie: ', 'Forge: ', 'Physique: ', 'Sport: ', 'Karate: ', 'Sud: ', 'Nord: ',
									'Capoeira: ', 'Bengale: ', 'Savoir: ', 'Informatique: ', 'Programmation: ', 'Python: ', 'Web2py: ',
									'Django: ', 'Methode: ', 'Uml: ', 'Merise: ');
			
			var a = help_confirm.constructList(label1, help_min.getArray());
			$('#minbox').html(a);
			
			var b = help_confirm.constructList(label2, help_skills.getArray());
			$('#skillbox').html(b);
			
			var c = '';
			if ( help_object.plasma ) c += 'Decoupeuse a plasma<br/>';
			if ( help_object.coudre ) c += 'Machine a Coudre<br/>';
			if ( help_object.voiture) c += 'Voiture<br/>';
			$('#objectbox').html(c);
			
			if ( callback ) callback();
			
			// Make scrollbar
			createScrollBar();
		});
	},
	
	constructList: function(labels, values) {
		var a = values.length;
		var b = '';
		for ( var i = 0; i < a; ++i ) {
			if ( values[i] == 0 ) {
				continue;
			}
			
			b += ('<div style="width:30%;float:left;">'+labels[i]+'</div><div>'+values[i]+'</div>');
		}
		
		return b;
	}
};



/*================================================================================================*/
/* Places Page */

function setupPlaces() {
	// Do important setup
	upkeep();
	radioButtonEvent();

	place_address.load(createScrollBar);

	$('#skill_next_btn').click(function() {
		switch ( GLOBAL_PAGE ) {
		
			case 'PLACE_1':
			if ( place_address.save() ) help_min.load(function() {
				$('#skill_title').html('<p>Ajout de lieux - Niveau minimal requis</p>');
			});
			break;
			
			case 'HELP_2':
			if ( help_min.save() ) help_skills.load(function() {
				$('#skill_title').html('<p>Ajout de lieux - Compétence</p>');
			});
			break;
			
			case 'HELP_3':
			if ( help_skills.save() ) help_object.load(function() {
				$('#skill_title').html('<p>Ajout de lieux - Objet</p>');
			});
			break;
			
			case 'HELP_4':
			if ( help_object.save() ) place_confirm.load(createScrollBar);
			break;
			
			case 'PLACE_2':
			
				// PUT DATA INTO DATABASE OR SOMETHING
				console.log(place_address);
				console.log(help_min);
				console.log(help_skills);
				console.log(help_object);
				
			break;
		}
	});
	
	$('#skill_back_btn').click(function() {
		switch ( GLOBAL_PAGE ) {
			case 'HELP_2':
			place_address.load(createScrollBar);
			break;
			
			case 'HELP_3':
			help_min.load(function() {
				$('#skill_title').html('<p>Ajout de lieux - Niveau minimal requis</p>');
			});
			break;
			
			case 'HELP_4':
			help_skills.load(function() {
				$('#skill_title').html('<p>Ajout de lieux - Compétence</p>');
			});
			break;
			
			case 'PLACE_2':
			help_object.load(function() {
				$('#skill_title').html('<p>Ajout de lieux - Objet</p>');
			});
			break;
		}
	});
}

var place_address = {
	name: 		'',
	address1: 	'',
	address2: 	'',
	address3: 	'',
	postal: 	'',
	city:		'',
	region:		'',
	country:	'',
	url1:		'',
	url2:		'',
	url3:		'',
	telephone:	'',
	hours:		'',
	tags:		'',
	
	load: function(callback) {
		GLOBAL_PAGE = 'PLACE_1';
		changeIndicator(0);
		
		$('#skill_window').load('include/add_place1.html', function() {
			place_address.recall();
		
			$('#skill_percentage').html('<p>0%</p>');

			$('#skill_content div.address-row').each(function() {
				$(this).height($(this).height());
			});
			
			if ( callback ) {
				callback();
			}
		});
	},
	
	save: function() {
		this.name 		= $('#place_name').val();
		this.address1 	= $('#place_address1').val();
		this.address2	= $('#place_address2').val();
		this.address3	= $('#place_address3').val();
		this.postal		= $('#place_postal').val();
		this.city		= $('#place_city').val();
		this.region		= $('#place_region').val();
		this.country	= $('#place_country').val();
		this.url1		= $('#place_url1').val();
		this.url2		= $('#place_url2').val();
		this.url3		= $('#place_url3').val();
		this.telephone 	= $('#place_telephone').val();
		this.hours		= $('#place_hours').val();
		this.tags		= $('#place_tags').val();
		
		var test = 	this.name == '' || 
					this.address1 == '' || 
					this.city == '' || 
					this.country == '' || 
					this.telephone == '' ||
					this.hours == '' || 
					this.tags == '';
		
		//console.log(this);
		
		return !test;
	},
	
	recall: function() {
		$('#place_name').val(this.name);
		$('#place_address1').val(this.address1);
		$('#place_address2').val(this.address2);
		$('#place_address3').val(this.address3);
		$('#place_postal').val(this.postal);
		$('#place_city').val(this.city);
		$('#place_region').val(this.region);
		$('#place_country').val(this.country);
		$('#place_url1').val(this.url1);
		$('#place_url2').val(this.url2);
		$('#place_url3').val(this.url3);
		$('#place_telephone').val(this.telephone);
		$('#place_hours').val(this.hours);
		$('#place_tags').val(this.tags);
	},
	
	getArray: function() {
		return new Array(this.name, this.address1, this.address2, this.address3, this.postal, this.city, this.region, this.country,
						this.url1, this.url2, this.url3, this.telephone, this.hours, this.tags);
	}
};

var place_confirm = {
	load: function(callback) {
		GLOBAL_PAGE = 'PLACE_2';
		changeIndicator(4);
		
		$('#skill_window').load('include/add_place2.html', function() {
			$('#skill_percentage').html('<p>80%</p>');
		
			var d = place_confirm.constructAddress();
			$('#addressbox').html(d);
			
			var label1 = new Array('Force: ', 'Logique: ', 'Volonte: ', 'Charisme: ', 'Apparence: ', 'Dexterite: ');
			var label2 = new Array('Technique: ', 'Metallerrie: ', 'Forge: ', 'Physique: ', 'Sport: ', 'Karate: ', 'Sud: ', 'Nord: ',
									'Capoeira: ', 'Bengale: ', 'Savoir: ', 'Informatique: ', 'Programmation: ', 'Python: ', 'Web2py: ',
									'Django: ', 'Methode: ', 'Uml: ', 'Merise: ');
			
			var a = help_confirm.constructList(label1, help_min.getArray());
			$('#minbox').html(a);
			
			var b = help_confirm.constructList(label2, help_skills.getArray());
			$('#skillbox').html(b);
			
			var c = '';
			if ( help_object.plasma ) c += 'Decoupeuse a plasma<br/>';
			if ( help_object.coudre ) c += 'Machine a Coudre<br/>';
			if ( help_object.voiture) c += 'Voiture<br/>';
			$('#objectbox').html(c);
			
			if ( callback ) callback();
		});
	},
	
	constructList: function(labels, values) {
		var a = values.length;
		var b = '';
		
		for ( var i = 0; i < a; ++i ) {
			if ( values[i] == 0 ) continue;		
			b += ('<div style="width:30%;float:left;">'+labels[i]+'</div><div>'+values[i]+'</div>');
		}
		
		return b;
	},
	
	constructAddress: function() {
		var row = function(a) {
			if ( a ) {
				return '<div class="addr-row">\
				<div></div>\
				<div>'+a+'</div>\
				</div>';
			}
			
			return '';
		};
	
		var d = place_address.getArray();
		var e = '<div>'+d[0]+'<br/></div>\
		<div class="addr-row">\
			<div>Adresse du nouveau lieu:</div>\
			<div>'+d[1]+'</div>\
		</div>'+row(d[2])+row(d[3])+'\
		<div class="addr-row">\
			<div>Code Postal:</div>\
			<div>'+d[4]+'</div>\
		</div>\
		<div class="addr-row">\
			<div>Ville:</div>\
			<div>'+d[5]+'</div>\
		</div>\
		<div class="addr-row">\
			<div>Region:</div>\
			<div>'+d[6]+'</div>\
		</div>\
		<div class="addr-row">\
			<div>Pays:</div>\
			<div>'+d[7]+'</div>\
		</div>\
		<div class="addr-row">\
			<div>Url:</div>\
			<div>'+d[8]+'</div>\
		</div>'+row(d[9])+row(d[10])+'\
		<div class="addr-row">\
			<div>Telephone:</div>\
			<div>'+d[11]+'</div>\
		</div>\
		<div class="addr-row">\
			<div>Horaires:</div>\
			<div>'+d[12]+'</div>\
		</div>\
		<div class="addr-row">\
			<div>Tags:</div>\
			<div>'+d[13]+'</div>\
		</div><br/>';

		return e;
	}
};



/*================================================================================================*/
/* Add Stuff Functions */

function createScrollBar() {
	var $d = $('#skill_content');
	var $j = $d.data('jsp');

	if ( $j ) {
		$j.reinitialise();
	} else {
		$d.jScrollPane({verticalGutter: 10});
		var $e = $d.data('jsp').getContentPane();
		
		if ( $e.next().hasClass('jspVerticalBar') ) {
			$e.addClass('filler');
		} else {
			$d.css({'background-color': 'rgba(0,0,0,0.5)'});
		}
	}
}

function radioButtonEvent() {
	var sp = $('#skill_percentage');
	sp.css({'font-size': sp.width()*0.4});
	
	// radio button graphics
	$('#skill_window').on('click', '.jp-radio-btn', function() {
		var s = $(this).siblings();
		var f = s.filter('.jp-radio-btn-selected');
		
		// something already selected
		if ( f.length != 0 ) {
			f.removeClass('jp-radio-btn-selected');
		}

		$(this).addClass('jp-radio-btn-selected');
	});
}

function fixRadioCSS() {
	// Fix font for small screen
	var b = $('#skill_legend .jp-radio-label');
	var c = b.eq(0);
	b.css({'font-size': c.width()*0.15});
}

function changeIndicator(n) {
	var a = $('#skill_navigation_wrapper div');
	a.filter('.nav-btn-current').removeClass('nav-btn-current');
	a.eq(n).addClass('nav-btn-current');
}
	
	

/*================================================================================================*/
/* Draw Object */

var DRAW = {
	banner: function(a) {
		var b 		= a.offset();
		var paper 	= Raphael(b.left, b.top, a.width(), a.height());
		var path 	= paper.path('m2,67h15l15,-66h-15l-15,66').attr({fill: 'rgba(0, 255, 50, 0.75)', stroke: 'none'});
		var path2 	= paper.path('m40,1h340l-15,66h-340z').attr({fill: 'rgba(0,0,0,0.5)', stroke: 'none'});
		
		// Jackpoint Text
		var text	= paper.text(70, 29, 'JackPoint')
		.attr({'text-anchor': 'start', 'font-family': 'loaded', 'font-size': 42, stroke: 'none', fill: 'rgba(0, 255, 50, 0.75)', href: 'index.html'})
		
		// Background for youtube icon
		var path3	= paper.path('m390,1h100l-15,66h-100l15,-66')
		.attr({fill: 'rgba(0, 0, 0, 0.5)', stroke: 'none', cursor: 'pointer', title: 'Youtube Video'})
		.hover(function() {
			yticon.attr('fill', '#000');
			this.attr('fill', 'rgba(0, 255, 50, 0.75)');
		}, function() {
			yticon.attr('fill', 'rgba(0, 255, 50, 0.75)');
			this.attr('fill', 'rgba(0, 0, 0, 0.5)');
		})
		.click(function() {
			var a = $('#youtube_wrapper');
			
			if ( !a.is(':visible') )
				a.show('blind', DRAW.ytcontrol($('#youtube_close'), $('#youtube_external')));
		});
	
		// Youtube Icon
		var yticon	= paper.path('m406,14h50s5,0,5,5v30s0,5,-5,5h-50s-5,0,-5,-5v-30s0,-5,5,-5m16,5v28l20,-13l-20,-15')
		.attr({fill:'rgba(0, 255, 50, 0.75)', stroke: 'none', cursor: 'pointer', title: 'Youtube Video'})
		.hover(function() {
			this.attr('fill', '#000');
			path3.attr('fill', 'rgba(0, 255, 50, 0.75)');
		}, function() {
			this.attr('fill', 'rgba(0, 255, 50, 0.75)');
			path3.attr('fill', 'rgba(0, 0, 0, 0.5)');
		})
		.click(function() {
			var a = $('#youtube_wrapper');
			
			if ( !a.is(':visible') )
				a.show('blind', DRAW.ytcontrol($('#youtube_close'), $('#youtube_external')));
		});
		
		// Background for facebook icon
		var path4 = paper.path('m500,1h100l-15,66h-100z')
		.attr({fill: 'rgba(0, 0, 0, 0.5)', stroke: 'none', cursor: 'pointer', title: 'Facebook', href: 'www.facebook.com'})
		.hover(function() {
			fbicon.attr('fill', '#000');
			this.attr('fill', 'rgba(0, 255, 50, 0.75)');
		}, function() {
			fbicon.attr('fill', 'rgba(0, 255, 50, 0.75)');
			this.attr('fill', 'rgba(0, 0, 0, 0.5)');
		});
		
		var fbicon = paper.path('m520,9h40s5,0,5,5v40s0,5,-5,5h-40s-5,0,-5,-5v-40s0,-5,5,-5m18,19v7h5v21h8v-21h5l3,-7h-7v-7h5l3,-8h-14s-2.5,0,-5,6v9z')
		.attr({fill:'rgba(0, 255, 50, 0.75)', stroke: 'none', cursor: 'pointer', title: 'Facebook', href: 'www.facebook.com'})
		.hover(function() {
			this.attr('fill', '#000');
			path4.attr('fill', 'rgba(0, 255, 50, 0.75)');
		}, function() {
			this.attr('fill', 'rgba(0, 255, 50, 0.75)');
			path4.attr('fill', 'rgba(0, 0, 0, 0.5)');
		});
		
		// scale
		var ratio = a.height() / 67;
		
		var set = paper.set();
		set.push(path, path2, text, path3, yticon, path4, fbicon).scale(ratio, ratio, 0, 0);
	},
	
	ytcontrol: function(a, b) {
		// close button
		if ( a.html() == '' ) {
			var o 		= a.offset();
			var paper 	= Raphael(o.left, o.top, a.width(), a.height());
			
			var cross 	= paper.path('m12,9l12,12l12,-12l6,6l-12,12l12,12l-6,6l-12,-12l-12,12l-6,-6l12,-12l-12,-12z')
			.attr({fill: 'rgba(0, 255, 50, 0.75)', stroke: 'rgba(0, 255, 50, 0.75)', title: 'Close', cursor: 'pointer'})
			.click(function() {
				$('#youtube_wrapper').hide();
			});
			
			a.append($(cross.node).parent().parent().css({top:0,left:0}));
		}
		
		// external button
		if ( b.html() == '' ) {
			var o 		= b.offset();
			var paper 	= Raphael(o.left, o.top, b.width(), b.height());
			
			var arrow	= paper.path('m5,20v10h20v10l20,-15l-20,-15v10z')
			.attr({fill: 'rgba(0, 255, 50, 0.75)', stroke: 'rgba(0, 255, 50, 0.75)', title: 'Video', cursor: 'pointer', href: 'http://youtu.be/CEGfDjdow9k', target: '_blank'});
			
			b.append($(arrow.node).parent().parent().css({top:0,left:0}));
		}
	}
};



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