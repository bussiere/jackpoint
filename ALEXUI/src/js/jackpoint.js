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
			
		case 'MAIN':
			setupMain();
			break;
			
		case 'SMS':
			setupSMS();
			break;
			
		case 'HELP_MAIN':
			setupHelpMain();
			break;
			
		case 'HELP_1':
			setupHelp();
			break;
		
		case 'PLACE_1':
			setupPlaces();
			break;
			
		case 'ADDEVENT_1':
			setupAddEvent();
			break;
	}
}

/*================================================================================================*/
/* Always Run */

function upkeep() {	
	var b = $('#avatarbox');
	b.width(b.height());
	
	var c = $('#usernamebox');
	c.css('font-size', c.height()*0.4);
	
	DRAW.simpleBanner($('#banner_wrapper'));
	
	// Raphael Version
	DRAW.navigation2($('#navigation_wrapper'));
	
	// external/externe version
	//$('#navigation_wrapper').load('gfx/navigation.svg', initializeNavigation);
}

/*
function initializeNavigation() {
	var a = $('#navigation_wrapper');
	var b = a.width() / 230;
	var c = a.height() / 537;
	
	// Not using raphael so we have to scale the svg the hard way
	// pas raphael, redimensionner et joindre événement dure-chemin
	$('#hexNav path,text').attr('transform', 'matrix('+c+',0,0,'+c+',0,0)');
	var d = $('#hexNav path.navhexagon');
	d.hover(function() {
		$(this).attr('fill', '#00ff32');
	}, function() {
		$(this).attr('fill', '#009619');
	});

	var e = $('#hexNav text.navlink');
	e.eq(0).hover(function() {
		d.eq(0).attr('fill', '#00ff32');
	}, function() {
		d.eq(0).attr('fill', '#009619');
	});
	e.eq(1).hover(function() {
		d.eq(1).attr('fill', '#00ff32');
	}, function() {
		d.eq(1).attr('fill', '#009619');
	});
	e.eq(2).hover(function() {
		d.eq(2).attr('fill', '#00ff32');
	}, function() {
		d.eq(2).attr('fill', '#009619');
	});
}
*/



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
/* Main Page */

function setupMain() {
	upkeep();
	DRAW.newsBorder($('#news_border'));
	
	var $a   		= $('#news_wrapper');
	var loadNews 	= function(e) {
	
		// Change the load target based on which button is pressed
		// Changer la cible en fonction du bouton sur lequel on appuie sur
		switch ( e.currentTarget.getAttribute('id') ) {
			case 'news_main_button':
			var path = 'include/sampleNews.html';
			break;
			
			case 'news_tag_button':
			var path = 'include/sampleNewsTag.html';
			break;
		}
	
		var b = $a.data('jsp');
		
		if ( b ) {
			var c = b.getContentPane();
			c.load(path, function() {
				$('#news_window section.news-section').each(function() {
					$(this).height($(this).height());
				});
				
				b.reinitialise();
			});
		} else {
			$a.load(path, function() {
				$('#news_window section.news-section').each(function() {
					$(this).height($(this).height());
				});
			
				$a.jScrollPane({verticalGutter: 10});
			});
		}
	};
	
	// Button font scale
	//var b = $('#news_button_wrapper');
	//b.css('font-size', b.height()*0.20);
	
	var c = $('#notification_list');
	c.css('font-size', c.children('div.notif-entry:first').height()*0.125);
	
	// Button event and load initial news
	$('#news_main_button').click(loadNews).click();
	$('#news_tag_button').click(loadNews);
	$('#notify_btn_refresh').click(function() {
		alert('refresh');
	});
	$('#notify_btn_eraseall').click(function() {
		alert('remove all');
	});
	
	// Draw the list window
	DRAW.notifications($('#notification_wrapper'));
	DRAW.mainBars($('#news_button_wrapper'));
	
	// Event for clicking on notification
	//$('#notification_list').on
	// Scale Bar
	//var r1 = $('#news_button_wrapper').width() / 627;
	//var r2 = $('#news_button_wrapper').height()/ 67;
	//$('#mainBar path:first').attr('transform', 'matrix('+r1+',0,0,'+r2+',0,0)');
}



/*================================================================================================*/
/* SMS Page */

function setupSMS() {
	upkeep();
	
	// convert to pixel height for scrollbar
	var a = $('#sms_container div.sms-wrapper');
	a.height(a.height());
	var b = $('#sms_container div.sms-reply-wrapper,div.sms-reply2-wrapper');
	b.height(b.height());
	
	var c = $('#sms_container div.sms-descript');
	c.css({'font-size':c.height()*0.1});
	
	var d = $('#sms_options');
	d.css({'font-size':d.height()*0.025});
	
	$('#sms_container').jScrollPane({verticalGutter: 10});
	
	DRAW.smsborder($('#sms_title'));
	DRAW.smsOption($('#sms_option_title'));
	//DRAW.smsDecoration($('#sms_container'));
	//console.log($('#sms_container').height());
}



/*================================================================================================*/
/* Help Page */

function setupHelpMain() {
	upkeep();
	
	// scale font
	var a = $('#help_wrapper div.help-item-content');
	a.css('font-size', a.height()*0.35);
	
	// hover event
	$('#help_wrapper').on({
		click: function() {
			
		},
		mouseenter: function() {
			//$(this).children('img').attr("src", "");
			$(this).css({'background-color': 'rgba(0, 255, 50, 0.75)', 'color': 'black'});
			$(this).closest('div.help-item-outer').css({'left':'10px'});
		},
		mouseleave: function() {
			//$(this).children('img').attr("src", "")	
			$(this).css({'background-color': 'rgba(0, 0, 0, 0.65)', 'color': '#00ff32'});
			$(this).closest('div.help-item-outer').css({'left':'0'});			
		}
	}, 'div.help-item-content');
	
	// do some custom drawing
	DRAW.helpBorder($('#help_title'));
	DRAW.previewBorder($('#help_preview'));
	DRAW.helpDeco($('#help_decoration'));
	
	// convert to pixel height
	var b = $('#help_wrapper div.help-item-outer');
	b.height(b.height());
	
	// initialize custom scrollbar
	$('#help_wrapper').jScrollPane({'verticalGutter': 15});
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
/* Add Places Page */

function setupPlaces() {
	// Do important setup
	upkeep();
	radioButtonEvent();

	place_address.load();

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
			place_address.load();
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
			
			createScrollBar();
			
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
		
		console.log(this);
		
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
			b += ('<div style="width:40%;float:left;">'+labels[i]+'</div><div>'+values[i]+'</div>');
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
/* Add Event Page */

function setupAddEvent() {
	// Do important setup
	upkeep();
	radioButtonEvent();
	
	place_address.load(function() {
		$('#skill_title').html('<p>Ajout d\'evenment - Addresse</p>');
	});
	
	$('#skill_next_btn').click(function() {
		switch ( GLOBAL_PAGE ) {
		
			case 'PLACE_1':
			if ( place_address.save() ) help_min.load(function() {
				$('#skill_title').html('<p>Ajout d\'evenment - Niveau minimal requis</p>');
			});
			break;
			
			case 'HELP_2':
			if ( help_min.save() ) help_skills.load(function() {
				$('#skill_title').html('<p>Ajout d\'evenment - Compétence</p>');
			});
			break;
			
			case 'HELP_3':
			if ( help_skills.save() ) help_object.load(function() {
				$('#skill_title').html('<p>Ajout d\'evenment - Objet</p>');
			});
			break;
			
			case 'HELP_4':
			if ( help_object.save() ) place_confirm.load(function() {
				$('#skill_title').html('<p>Ajout d\'evenment - Confirmer</p>');
				createScrollBar();
			});
			break;
			
			case 'ADDEVENT_2':
			
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
			place_address.load(function() {
				$('#skill_title').html('<p>Ajout d\'evenment - Addresse</p>');
			});
			break;
			
			case 'HELP_3':
			help_min.load(function() {
				$('#skill_title').html('<p>Ajout d\'evenment - Niveau minimal requis</p>');
			});
			break;
			
			case 'HELP_4':
			help_skills.load(function() {
				$('#skill_title').html('<p>Ajout d\'evenment - Compétence</p>');
			});
			break;
			
			case 'ADDEVENT_2':
			help_object.load(function() {
				$('#skill_title').html('<p>Ajout d\'evenment - Objet</p>');
			});
			break;
		}
	});
}



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

/* Big Tip: Select the svg element in FIREBUG and copy/paste the path string into the path in firebug.
			Then you can easily change the shape of the line */

var DRAW = {
	simpleBanner: function(a) {
		if ( a.length == 0 )
			return;
	
		var b 		= a.offset();
		var paper 	= Raphael(b.left, b.top, a.width(), a.height());
		var rh 		= a.height() / 74;
		var rw 		= a.width() / 1280;
	
		var logobox = paper.path('m-1,-1h379v53l-20,20h-379')
		.attr({fill: 'rgba(0,0,0,0.65)', stroke: 'rgba(0, 255, 50, 0.75)'});
		
		var logo	= paper.path('M7,7L27,7V18H19V28H7V24H15V18H7V14H15M19,14H23V11H19V14M15,14V11H7V7')
		.attr({fill: 'rgba(0, 255, 50, 0.75)', stroke: 'none', cursor: 'pointer', href: 'main.html'})
		.transform('t-7,-7s'+(2*rw)+','+(2*rw)+',0,0');
		
		var logotex = paper.text(87, 27, 'JackPoint')
		.attr({'text-anchor': 'start', 'font-family': 'loaded', 'font-size': 38, stroke: 'none', fill: 'rgba(0, 255, 50, 0.75)', href: 'main.html'})
		.transform('s'+rw+','+rw+',0,0');

		
		// Extra Line
		var line1	= paper.path('m379,33h420v-9l20,-21h460v50l-20,20h-460v-40').attr({fill: 'none', stroke: 'rgba(0, 255, 50, 0.75)'});
		var context = paper.text(390, 17, 'Connection Established; Database Online; Hydra Encryption Enabled')
		.attr({fill: 'rgba(0, 255, 50, 0.75)', stroke: 'none', 'font-family': 'DX', 'font-size': 11, 'text-anchor': 'start'});
		
		// UserBox
		var uBox	= paper.path('M803,34v-8l19,-19h452v45l-17,17h-454z').attr({fill: 'rgba(0, 255, 50, 0.75)', stroke: 'none'});
		
		// User Settings
		var IconTextAttr = {fill: 'black', stroke: 'none', 'text-anchor': 'start', 'font-family': 'DX', 'font-size': 12, cursor: 'pointer'};
		
		var settings = paper.path('M17.41,20.395l-0.778-2.723c0.228-0.2,0.442-0.414,0.644-0.643l2.721,0.778c0.287-0.418,0.534-0.862,0.755-1.323l-2.025-1.96c0.097-0.288,0.181-0.581,0.241-0.883l2.729-0.684c0.02-0.252,0.039-0.505,0.039-0.763s-0.02-0.51-0.039-0.762l-2.729-0.684c-0.061-0.302-0.145-0.595-0.241-0.883l2.026-1.96c-0.222-0.46-0.469-0.905-0.756-1.323l-2.721,0.777c-0.201-0.228-0.416-0.442-0.644-0.643l0.778-2.722c-0.418-0.286-0.863-0.534-1.324-0.755l-1.96,2.026c-0.287-0.097-0.581-0.18-0.883-0.241l-0.683-2.73c-0.253-0.019-0.505-0.039-0.763-0.039s-0.51,0.02-0.762,0.039l-0.684,2.73c-0.302,0.061-0.595,0.144-0.883,0.241l-1.96-2.026C7.048,3.463,6.604,3.71,6.186,3.997l0.778,2.722C6.736,6.919,6.521,7.134,6.321,7.361L3.599,6.583C3.312,7.001,3.065,7.446,2.844,7.907l2.026,1.96c-0.096,0.288-0.18,0.581-0.241,0.883l-2.73,0.684c-0.019,0.252-0.039,0.505-0.039,0.762s0.02,0.51,0.039,0.763l2.73,0.684c0.061,0.302,0.145,0.595,0.241,0.883l-2.026,1.96c0.221,0.46,0.468,0.905,0.755,1.323l2.722-0.778c0.2,0.229,0.415,0.442,0.643,0.643l-0.778,2.723c0.418,0.286,0.863,0.533,1.323,0.755l1.96-2.026c0.288,0.097,0.581,0.181,0.883,0.241l0.684,2.729c0.252,0.02,0.505,0.039,0.763,0.039s0.51-0.02,0.763-0.039l0.683-2.729c0.302-0.061,0.596-0.145,0.883-0.241l1.96,2.026C16.547,20.928,16.992,20.681,17.41,20.395zM11.798,15.594c-1.877,0-3.399-1.522-3.399-3.399s1.522-3.398,3.399-3.398s3.398,1.521,3.398,3.398S13.675,15.594,11.798,15.594zM27.29,22.699c0.019-0.547-0.06-1.104-0.23-1.654l1.244-1.773c-0.188-0.35-0.4-0.682-0.641-0.984l-2.122,0.445c-0.428-0.364-0.915-0.648-1.436-0.851l-0.611-2.079c-0.386-0.068-0.777-0.105-1.173-0.106l-0.974,1.936c-0.279,0.054-0.558,0.128-0.832,0.233c-0.257,0.098-0.497,0.22-0.727,0.353L17.782,17.4c-0.297,0.262-0.568,0.545-0.813,0.852l0.907,1.968c-0.259,0.495-0.437,1.028-0.519,1.585l-1.891,1.06c0.019,0.388,0.076,0.776,0.164,1.165l2.104,0.519c0.231,0.524,0.541,0.993,0.916,1.393l-0.352,2.138c0.32,0.23,0.66,0.428,1.013,0.6l1.715-1.32c0.536,0.141,1.097,0.195,1.662,0.15l1.452,1.607c0.2-0.057,0.399-0.118,0.596-0.193c0.175-0.066,0.34-0.144,0.505-0.223l0.037-2.165c0.455-0.339,0.843-0.747,1.152-1.206l2.161-0.134c0.152-0.359,0.279-0.732,0.368-1.115L27.29,22.699zM23.127,24.706c-1.201,0.458-2.545-0.144-3.004-1.345s0.143-2.546,1.344-3.005c1.201-0.458,2.547,0.144,3.006,1.345C24.931,22.902,24.328,24.247,23.127,24.706z')
		.attr({fill: 'black', stroke: 'none', cursor: 'pointer'})
		.transform('s'+(1.6*rh)+','+(1.6*rh)+',0,0T'+(1070*rw)+','+(10*rh));
		
		var settingsText = paper.text(1110, 20, 'Settings')
		.attr(IconTextAttr);
		
		// Logout Area
		var logout = paper.path('M25.542,8.354c-1.47-1.766-2.896-2.617-3.025-2.695c-0.954-0.565-2.181-0.241-2.739,0.724c-0.556,0.961-0.24,2.194,0.705,2.763c0,0,0.001,0,0.002,0.001c0.001,0,0.002,0.001,0.003,0.002c0.001,0,0.003,0.001,0.004,0.001c0.102,0.062,1.124,0.729,2.08,1.925c1.003,1.261,1.933,3.017,1.937,5.438c-0.001,2.519-1.005,4.783-2.64,6.438c-1.637,1.652-3.877,2.668-6.368,2.669c-2.491-0.001-4.731-1.017-6.369-2.669c-1.635-1.654-2.639-3.919-2.64-6.438c0.005-2.499,0.995-4.292,2.035-5.558c0.517-0.625,1.043-1.098,1.425-1.401c0.191-0.152,0.346-0.263,0.445-0.329c0.049-0.034,0.085-0.058,0.104-0.069c0.005-0.004,0.009-0.006,0.012-0.008s0.004-0.002,0.004-0.002l0,0c0.946-0.567,1.262-1.802,0.705-2.763c-0.559-0.965-1.785-1.288-2.739-0.724c-0.128,0.079-1.555,0.93-3.024,2.696c-1.462,1.751-2.974,4.511-2.97,8.157C2.49,23.775,8.315,29.664,15.5,29.667c7.186-0.003,13.01-5.892,13.012-13.155C28.516,12.864,27.005,10.105,25.542,8.354zM15.5,17.523c1.105,0,2.002-0.907,2.002-2.023h-0.001V3.357c0-1.118-0.896-2.024-2.001-2.024s-2.002,0.906-2.002,2.024V15.5C13.498,16.616,14.395,17.523,15.5,17.523z')
		.attr({fill: 'black', stroke: 'none', cursor: 'pointer'})
		.transform('s'+(1.4*rh)+','+(1.4*rh)+',0,0T'+(1170*rw)+','+(15*rh));
		
		var logoutText = paper.text(1215, 20, 'Logout')
		.attr(IconTextAttr);
		
		var s = paper.set();
		s.push(logobox, line1, context, uBox, settingsText, logoutText).scale(rw, rh, 0, 0);
	},

	banner: function(a) {
		var b 		= a.offset();
		var paper 	= Raphael(b.left, b.top, a.width(), a.height());
		
		// scale
		var ratio  = a.height() / 67;
		var ratio2 = a.width() / 640;
		
		// Jackpoint Text
		var handle 	= paper.path('m2,67h15l15,-66h-15l-15,66').attr({fill: 'rgba(0, 255, 50, 0.75)', stroke: 'none'});
		var jpback 	= paper.path('m40,1h340l-15,66h-340z').attr({fill: 'rgba(0,0,0,0.5)', stroke: 'none'});
		var text	= paper.text(70, 29, 'JackPoint')
		.attr({'text-anchor': 'start', 'font-family': 'loaded', 'font-size': 42, stroke: 'none', fill: 'rgba(0, 255, 50, 0.75)', href: 'index.html'})
		
		// YOUTUBE
		var youtubeBack	= paper.path('m390,1h100l-15,66h-100l15,-66').attr('fill', 'rgba(0, 0, 0, 0.5)');
		var youtubeIcon	= paper.path('m406,14h50s5,0,5,5v30s0,5,-5,5h-50s-5,0,-5,-5v-30s0,-5,5,-5m16,5v28l20,-13l-20,-15').attr('fill','rgba(0, 255, 50, 0.75)');
		
		var youtube = paper.set()
		.push(youtubeBack, youtubeIcon)
		.attr({stroke: 'none', cursor: 'pointer', title: 'Youtube Video'})
		.hover(function() {
			youtubeIcon.attr('fill', '#000');
			youtubeBack.attr('fill', 'rgba(0, 255, 50, 0.75)');
		}, function() {
			youtubeIcon.attr('fill', 'rgba(0, 255, 50, 0.75)');
			youtubeBack.attr('fill', 'rgba(0, 0, 0, 0.5)');
		}).click(DRAW.showYoutube);

		
		// TWITTER
		var twitterBack = paper.path('m500,1h100l-15,66h-100z').attr('fill', 'rgba(0, 0, 0, 0.5)');
		var twitterIcon = paper.path('M14.605,13.11c0.913-2.851,2.029-4.698,3.313-6.038c0.959-1,1.453-1.316,0.891-0.216c0.25-0.199,0.606-0.464,0.885-0.605c1.555-0.733,1.442-0.119,0.373,0.54c2.923-1.045,2.82,0.286-0.271,0.949c2.527,0.047,5.214,1.656,5.987,5.077c0.105,0.474-0.021,0.428,0.464,0.514c1.047,0.186,2.03,0.174,2.991-0.13c-0.104,0.708-1.039,1.167-2.497,1.471c-0.541,0.112-0.651,0.083-0.005,0.229c0.799,0.179,1.69,0.226,2.634,0.182c-0.734,0.846-1.905,1.278-3.354,1.296c-0.904,3.309-2.976,5.678-5.596,7.164c-6.152,3.492-15.108,2.984-19.599-3.359c2.947,2.312,7.312,2.821,10.555-0.401c-2.125,0-2.674-1.591-0.99-2.449c-1.595-0.017-2.608-0.521-3.203-1.434c-0.226-0.347-0.229-0.374,0.14-0.64c0.405-0.293,0.958-0.423,1.528-0.467c-1.651-0.473-2.66-1.335-3.009-2.491c-0.116-0.382-0.134-0.363,0.256-0.462c0.38-0.097,0.87-0.148,1.309-0.17C6.11,10.88,5.336,9.917,5.139,8.852c-0.186-1.006,0.005-0.748,0.758-0.46C9.263,9.68,12.619,11.062,14.605,13.11L14.605,13.11z')
		.attr('fill', 'rgba(0, 255, 50, 0.75)')
		.transform('S2,2,0,0T'+(510*ratio2)+',0');
		
		var twitter = paper.set()
		.push(twitterBack, twitterIcon)
		.attr({stroke: 'none', cursor: 'pointer', title: 'Twitter', href: 'https://twitter.com/'})
		.hover(function() {
			twitterIcon.attr('fill', '#000');
			twitterBack.attr('fill', 'rgba(0, 255, 50, 0.75)');
		}, function() {
			twitterIcon.attr('fill', 'rgba(0, 255, 50, 0.75)');
			twitterBack.attr('fill', 'rgba(0, 0, 0, 0.5)');
		});
		
		var set = paper.set();
		set.push(handle, jpback, text, youtube, twitter).scale(ratio2, ratio, 0, 0);
	},
	
	showYoutube: function() {
		var a = $('#youtube_wrapper');
			
		if ( !a.is(':visible') )
			a.show('blind', DRAW.ytcontrol($('#youtube_close'), $('#youtube_external')));
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
	},
	
	createHexGroup: function(hex, text) {
		var a = hex.p.path(hex.path).attr(hex.at)
		.hover(function() {
			this.attr('fill', '#00ff32');
		}, function() {
			this.attr('fill', 'rgba(0, 150, 25, 0.75)');
		});;
		
		var c = hex.p.text(text.x, text.y, text.word).attr(text.at)
		.hover(function() {
			a.attr('fill', '#00ff32');
		}, function() {
			a.attr('fill', 'rgba(0, 150, 25, 0.75)');
		});
		
		var d = hex.p.set();
		d.push(a, c);
		
		return d;
	},
	
	navigation2: function(a) {
		if ( a.length == 0 )
			return;
			
		var b  = a.offset();
		var p  = Raphael(b.left, b.top, a.width(), a.height());
		var rw = a.width() / 230;
		var rh = a.height() / 537;
		
		var hex_attr 	= { fill: 'rgba(0, 150, 25, 0.75)', stroke: 'none', cursor: 'pointer' };
		var hex_attr_e  = { fill: 'none', stroke: 'rgba(0, 150, 25, 0.75)' };
		var t1_attr		= { fill: 'rgba(0, 150, 25, 0.75)', stroke: 'none', 'font-family': 'Verdana', 'text-anchor': 'start', 'font-size': 14, cursor: 'pointer' };
		var t2_attr		= { fill: 'black', stroke: 'none', 'font-family': 'DX', 'text-anchor': 'end', 'font-size': 14 };
		
		// Border
		var c = p.path('m0,40v50h10v-40l40,-40h180v-10h-190zM230,497v-50h-10v40l-40,40h-180v10h190z')
		.attr({fill: '#00ff32', stroke: 'none', 'fill-opacity': 0.75});
		
		// Decoration
		var d 		= p.path('m230,30h-120M230,55h-50M230,80h-55M0,515h100M0,495h40')
		.attr({fill: 'none', stroke: 'rgba(0, 150, 25, 0.75)'});
		var phi 	= p.text(47, 29, 'φ0xFFFF').attr(t1_attr);
		var lambda 	= p.text(112, 54, 'λ0x0AE5').attr(t1_attr);
		var sigma	= p.text(135, 79, 'Σ0x0').attr(t1_attr);
		var delta	= p.text(48, 494, 'Δ0111001').attr(t1_attr);
		var omega	= p.text(108, 513, 'Ω99%').attr(t1_attr);
		var dtext 	= p.set().push(phi, lambda, sigma, delta, omega);
		
		// Hexagon
		var hex1 = DRAW.createHexGroup({p: p, path: 'm60,70h45l23,40l-23,40h-45l-23,-39z', at: hex_attr}, {x:115, y: 108, word: $('#hexagon_main').text(), at: t2_attr}).attr('href', 'main.html');
		var hex2 = DRAW.createHexGroup({p: p, path: 'm130,110h45l23,40l-23,40h-45l-23,-39z', at: hex_attr}, {x:185, y: 149, word: $('#hexagon_sms').text(), at: t2_attr}).attr('href', 'sms.html');
		var hex3 = DRAW.createHexGroup({p: p, path: 'm60,152h45l23,40l-23,40h-45l-23,-39z', at: hex_attr}, {x:115, y: 190, word: $('#hexagon_help').text(), at: t2_attr}).attr('href', 'help.html');
		var hex4 = DRAW.createHexGroup({p: p, path: 'm130,192h45l23,40l-23,40h-45l-23,-39z', at: hex_attr}, {x:185, y: 230, word: $('#hexagon_event').text(), at: t2_attr}).attr('href', 'add_event.html');
		var hex5 = DRAW.createHexGroup({p: p, path: 'm60,234h45l23,40l-23,40h-45l-23,-39z', at: hex_attr}, {x:115, y: 275, word: $('#hexagon_place').text(), at: t2_attr}).attr('href', 'add_place.html');
		var hex6 = DRAW.createHexGroup({p: p, path: 'm130,274h45l23,40l-23,40h-45l-23,-39z', at: hex_attr}, {x:185, y: 312, word: $('#hexagon_msg').text(), at: t2_attr}).attr('href', 'msg.html');
		var hex7 = p.path('m60,317h45l23,40l-23,40h-45l-23,-39z').attr(hex_attr_e);
		var hex8 = p.path('m130,357h45l23,40l-23,40h-45l-23,-39z').attr(hex_attr_e);
		var hex9 = p.path('m60,400h45l23,40l-23,40h-45l-23,-39z').attr(hex_attr_e);
		var h = p.set().push(hex1, hex2, hex3, hex4, hex5, hex6, hex7, hex8, hex9);
		
		var set = p.set().push(c, d, dtext, h).transform('S'+rh+','+rh+',0,0');
	},
	
	// =================================================================
	// MAIN DRAWING
	
	newsBorder: function(a) {
		var b = a.offset();
		var p = Raphael(b.left, b.top, a.width(), a.height());
		var r1 = a.width() / 616;
		var r2 = a.height()/ 436;
		
		var border = p.path('m26,1h589v410l-24,24h-589v-410z').attr({fill: 'rgba(0,0,0,0.65)', stroke: '#00ff32'});
		border.scale(r1, r2, 0, 0);
		$(border.node).parent().css({'z-index': '-1' });
	},
	
	notifications: function(a) {
		var b = a.offset();
		var p = Raphael(b.left, b.top, a.width(), a.height());

		var r1 = a.width() / 294;
		var r2 = a.height()/ 537;
		
		var border = p.path('m1,21l20,-20h272v40l-20,20H1z')
		.attr({fill: 'rgba(0,0,0,0.65)', stroke: '#00ff32'});
		
		var icon = p.path('M29.225,23.567l-3.778-6.542c-1.139-1.972-3.002-5.2-4.141-7.172l-3.778-6.542c-1.14-1.973-3.003-1.973-4.142,0L9.609,9.853c-1.139,1.972-3.003,5.201-4.142,7.172L1.69,23.567c-1.139,1.974-0.207,3.587,2.071,3.587h23.391C29.432,27.154,30.363,25.541,29.225,23.567zM16.536,24.58h-2.241v-2.151h2.241V24.58zM16.428,20.844h-2.023l-0.201-9.204h2.407L16.428,20.844z')
		.attr({fill: 'rgba(0, 255, 50, 0.75)', stroke: 'none'})
		.transform('S1.3,1.3,0,0T23,10S'+r2+','+r2+',0,0');
		
		var title = p.text(73, 30, 'NOTIFICATIONS')
		.attr({fill: '#00ff32', stroke: 'none', 'text-anchor': 'start', 'font-family':'DX', 'font-size': 26});
		
		var s = p.set().push(border, title).transform('S'+r1+','+r2+',0,0');
	},
	
	// =================================================================
	// SMS PAGE
	
	smsborder: function(a) {
		var b = a.offset();
		var p = Raphael(b.left, b.top, a.width(), a.height());
		var r1 = a.width() / 704;
		var r2 = a.height()/ 67;
		
		var border = p.path('M1,21l20,-20h430v45l-20,20H1zM485,21l20,-20h70v45l-20,20h-70zM600,21l20,-20h70v45l-20,20h-70z')
		.attr({fill: 'rgba(0,0,0,0.65)', stroke: '#00ff32'});
		
		var smsicon = p.path('m40,20h40l-20,10zm0,2v24h40v-24l-20,10z')
		.attr({fill: 'rgba(0, 255, 50, 0.75)', stroke: 'none'});
		
		var title = p.text(100, 31, 'SMS MESSAGES')
		.attr({fill: '#00ff32', stroke: 'none', 'font-family': 'DX', 'font-size': 24, 'text-anchor': 'start'});
		
		var refresh = p.path('M19.275,3.849l1.695,8.56l1.875-1.642c2.311,3.59,1.72,8.415-1.584,11.317c-2.24,1.96-5.186,2.57-7.875,1.908l-0.84,3.396c3.75,0.931,7.891,0.066,11.02-2.672c4.768-4.173,5.521-11.219,1.94-16.279l2.028-1.775L19.275,3.849zM8.154,20.232c-2.312-3.589-1.721-8.416,1.582-11.317c2.239-1.959,5.186-2.572,7.875-1.909l0.842-3.398c-3.752-0.93-7.893-0.067-11.022,2.672c-4.765,4.174-5.519,11.223-1.939,16.283l-2.026,1.772l8.26,2.812l-1.693-8.559L8.154,20.232z')
		.attr({fill: 'rgba(0, 255, 50, 0.75)', stroke: 'none', href: '#', title: 'Refresh'})
		.transform('s1.5,1.5,0,0T506,10S'+r1+','+r2+',0,0');
		
		var unanswered = p.path('m639,15h12.5v12.5h12.5v12.5h-12.5v12.5h-12.5v-12.5h-12.5v-12.5h12.5z')
		.attr({fill: 'rgba(0, 255, 50, 0.75)', stroke: 'none', href: '#'});

		var s = p.set().push(border, smsicon, unanswered, title).transform('s'+r1+','+r2+',0,0');
	},
	
	smsOption: function(a) {
		var b = a.offset();
		var p = Raphael(b.left, b.top, a.width(), a.height());
		
		var r1 = a.width() / 269;
		var r2 = a.height()/ 67;
		
		var border = p.path('M1,1h266v65H21l-20,-20z')
		.attr({fill: 'rgba(0,0,0,0.65)', stroke: '#00ff32'});
		
		var t = p.text(70, 30, 'PLACEHOLDER')
		.attr({fill: '#00ff32', stroke: 'none', 'font-family': 'DX', 'font-size': 24, 'text-anchor': 'start'});
		
		var s = p.set().push(border,t).transform('s'+r1+','+r2+',0,0');
	},
	
	smsDecoration: function(a) {
		var b = a.offset();
		var p = Raphael(b.left, b.top, a.width(), a.height());
		var r1 = a.width() / 704;
		var r2 = a.height()/ 456;
		
		var node = p.path('m6,381l41,-23l39,23l-40,23zm-1,48v-46l40,23v45zm42,22l41,-24v-44l-41,23z')
		//m0-120v-100m50,120l152,-152m0,0v34l41,11v-96l-41,9zm41,-51l12,2v90l-12,4zm12,5l5,-2l8,2v83l-7,2l-6,0zm13,60h200m0,0v50m-266,-106l-80,-80
		.attr({fill: 'rgba(0, 150, 25, 0.25)', stroke: 'rgba(0, 150, 25, 0.25)'})
		.transform('T575,350');
		var s = p.set().push(node).transform('s'+r1+','+r2+',0,0');
	},
	
	// =================================================================
	// Help Main Page
	
	helpBorder: function(a) {
		var b = a.offset();
		var p = Raphael(b.left, b.top, a.width(), a.height());
		var r1 = a.width() / 704;
		var r2 = a.height()/ 67;
		
		var border = p.path('M1,21l20,-20h670v45l-20,20H1z')
		.attr({fill: 'rgba(0,0,0,0.65)', stroke: '#00ff32'});
		
		var smsicon = p.path('M16,4.938c-7.732,0-14,4.701-14,10.5c0,1.981,0.741,3.833,2.016,5.414L2,25.272l5.613-1.44c2.339,1.316,5.237,2.106,8.387,2.106c7.732,0,14-4.701,14-10.5S23.732,4.938,16,4.938zM16.982,21.375h-1.969v-1.889h1.969V21.375zM16.982,17.469v0.625h-1.969v-0.769c0-2.321,2.641-2.689,2.641-4.337c0-0.752-0.672-1.329-1.553-1.329c-0.912,0-1.713,0.672-1.713,0.672l-1.12-1.393c0,0,1.104-1.153,3.009-1.153c1.81,0,3.49,1.121,3.49,3.009C19.768,15.437,16.982,15.741,16.982,17.469z')
		.attr({fill: 'rgba(0, 255, 50, 0.75)', stroke: 'none'})
		.transform('s1.8,1.8,0,0T28,5S'+r2+','+r2+',0,0');
		
		var title = p.text(100, 32, 'AIDE NÉCESSAIRE')
		.attr({fill: '#00ff32', stroke: 'none', 'font-family': 'DX', 'font-size': 24, 'text-anchor': 'start'});
		
		//var refresh = p.path('M19.275,3.849l1.695,8.56l1.875-1.642c2.311,3.59,1.72,8.415-1.584,11.317c-2.24,1.96-5.186,2.57-7.875,1.908l-0.84,3.396c3.75,0.931,7.891,0.066,11.02-2.672c4.768-4.173,5.521-11.219,1.94-16.279l2.028-1.775L19.275,3.849zM8.154,20.232c-2.312-3.589-1.721-8.416,1.582-11.317c2.239-1.959,5.186-2.572,7.875-1.909l0.842-3.398c-3.752-0.93-7.893-0.067-11.022,2.672c-4.765,4.174-5.519,11.223-1.939,16.283l-2.026,1.772l8.26,2.812l-1.693-8.559L8.154,20.232z')
		//.attr({fill: 'rgba(0, 255, 50, 0.75)', stroke: 'none', href: '#', title: 'Refresh'})
		//.transform('s1.5,1.5,0,0T506,10S'+r1+','+r2+',0,0');
		
		//var unanswered = p.path('m639,15h12.5v12.5h12.5v12.5h-12.5v12.5h-12.5v-12.5h-12.5v-12.5h12.5z')
		//.attr({fill: 'rgba(0, 255, 50, 0.75)', stroke: 'none', href: '#'});

		var s = p.set().push(border, title).transform('s'+r1+','+r2+',0,0');
	},
	
	previewBorder: function(a) {
		var b = a.offset();
		var p = Raphael(b.left, b.top, a.width(), a.height());
		var r1 = a.width() / 269;
		var r2 = a.height()/ 463;
		
		var border = p.path('M1,31l30,-30h237v431l-30,30H1z')
		.attr({fill: 'rgba(0,0,0,0.65)', stroke: '#00ff32'})
		.transform('s'+r1+','+r2+',0,0');
		
		//var title = p.text(110, 30, 'PREVIEW')
		//.attr({fill: '#00ff32', stroke: 'none', 'font-family': 'DX', 'font-size': 24, 'text-anchor': 'start'});
	},
	
	helpDeco: function(a) {
		var b = a.offset();
		var p = Raphael(b.left, b.top, a.width(), a.height());
		var r1 = a.width() / 627;
		var r2 = a.height()/ 60;

		var ico = p.path('m0,0l41,-23l39,23l-40,23zm-1,48v-46l40,23v45zm42,22l41,-24v-44l-41,23z')
		.attr({fill: 'rgba(0, 150, 25, 0.25)', stroke: 'rgba(0, 150, 25, 0.25)'})
		.transform('s0.5,0.5,0,0T25,25S'+r2+','+r2+',0,0');
		
		var ico2 = ico.clone().transform('s0.5,0.5,0,0T100,23S'+r2+','+r2+',0,0');
		var ico3 = p.path('m0,0l41,-23l39,23l-40,23zm-1,48v-46l40,23v45zm42,22l41,-24v-44l-41,23zm40,-40h330m0,0v45h90v-80l-20,-20h-70zm90,0h40m0,-40v80')
		.attr({fill: 'rgba(0, 150, 25, 0.25)', stroke: 'rgba(0, 150, 25, 0.25)'})
		.transform('s0.5,0.5,0,0T175,25S'+r2+','+r2+',0,0');
		
		var dtext = p.text(455, 35, '58902394773762029387\n06934045409442756849\n24442614769918725065\n13466864096638051527')
		.attr({fill: 'rgba(0, 150, 25, 0.25)', stroke: 'none', 'font-family': 'DX', 'font-size': 11, 'text-anchor': 'start'})
		.transform('s'+r2+','+r2+',0,0');
		
		
	},
	
	
	mainBars: function(a) {
		var b = a.offset();
		var p = Raphael(b.left, b.top, a.width(), a.height());
		
		var r1 = a.width() / 627;
		var r2 = a.height()/ 67;
		
		var bar = p.path('m230,6h140v13h-140m0,5h300v14h-300m0,5h200v13h-200v-50h-2v50h2')
		.attr({fill: 'rgba(0, 255, 50, 0.75)', stroke: 'none'})
		.transform('S'+r2+','+r2+',0,0');
		
		//var t = p.text(555, 33, '2548184317\n5375124182\n3786850786\n3445011020')
		//.attr({fill: 'rgba(0, 150, 25, 0.25)', stroke: 'none', 'font-family': 'DX', 'font-size': 11, 'text-anchor': 'start'})
		//.transform('S'+r2+','+r2+',0,0');
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
