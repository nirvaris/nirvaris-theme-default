var GALLERY = GALLERY || {};

(function($){

	// USE STRICT
	"use strict";
	
	GALLERY.initialize = {

		init: function(){

			GALLERY.initialize.createThumbs();
			GALLERY.initialize.startGallery();

		},
		
		createThumbs: function(){
			for (var i = 0; i < galleryData.length; i ++) {
				var galleryItem = galleryData[i];
				var html = '<li><img src="' + galleryItem.tinny + '" /></li>';
				$galleryThumbsEl.append(html);
			}
			$galleryThumbsEls = $galleryThumbsEl.find('li');
			
			$galleryThumbsWrapperEl.css('padding-left', thumbsWrapperPadding);
			$galleryThumbsWrapperEl.css('padding-right', thumbsWrapperPadding);
			$galleryThumbsEl.css('left', 0);
			
			$galleryThumbsEls.each(function(index){
				$(this).click(function(){
					GALLERY.widget.showGalleryImage(index);
				});
			});
			
			$scrollLeftButton.click(function(){
				var scrollSize = 0;
				
				if (GALLERY.widget.getScrollSize('right') < 0) {
					scrollSize = GALLERY.widget.getScrollSize('right');
				} else {
					scrollSize = 0;
				}
				
				if (($galleryThumbsEl.position().left - thumbsWrapperPadding) < 0) {
					$galleryThumbsEl.css('left', scrollSize);
				}
			});
			
			$scrollRightButton.click(function(){
				var galleryEl = $('.gallery');
				var scrollSize = 0;
				
				if (GALLERY.widget.getScrollSize('left') > -(($galleryThumbsEl.width() + (2 * thumbsWrapperPadding)) - galleryEl.width())) {
					scrollSize = GALLERY.widget.getScrollSize('left');
				} else {
					scrollSize = -($galleryThumbsEl.width() - (galleryEl.width() - (2 * thumbsWrapperPadding)));
				}
				
				if ($galleryThumbsEl.position().left > -($galleryThumbsEl.width() - galleryEl.width())) {
					$galleryThumbsEl.css('left', scrollSize);
				}
				
			});
		},
		
		startGallery: function(){
			GALLERY.widget.showGalleryImage(0);
		}
	},
	
	GALLERY.widget = {
		showGalleryImage: function(imageIndex){
			var galleryItem = galleryData[imageIndex];
			var thumbItem = $galleryThumbsEls[imageIndex]
			$galleryImageEl.attr('src', galleryItem.small);
			$galleryDescriptionEl.html(galleryItem.description);		
			$(thumbItem).addClass('active');	
		},
		getScrollSize: function(direction){
			var scrollSize = 0;
			
			if (direction == 'left') {
				scrollSize = (($galleryThumbsEl.position().left - thumbsScrollSize) - thumbsWrapperPadding);
			} else {
				scrollSize = (($galleryThumbsEl.position().left + thumbsScrollSize) - thumbsWrapperPadding);
			}
	
			return scrollSize;
		}
	},
	
	GALLERY.documentOnReady = {

		init: function(){
			GALLERY.initialize.init();
		}

	};
	
	var $galleryEl = $('.gallery'),
		$galleryThumbsWrapperEl = $('.gallery-thumbs'),
		$galleryThumbsEl = $('.gallery-thumbs ul'),
		$galleryImageEl = $('.gallery-image'),
		$galleryDescriptionEl = $('.gallery-image-description span'),
		$galleryThumbsEls = [],
		$scrollLeftButton = $('.gallery-scroll-left-button'),
		$scrollRightButton = $('.gallery-scroll-right-button'),
		thumbsWrapperPadding = 30,
		thumbsScrollSize = 270 // 2x thumb width + 2x thumb right margin,
	;
	
	$(document).ready( GALLERY.documentOnReady.init );
	
})(jQuery);