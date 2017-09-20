/* Javascript for CaptionedImageXBlock. */
function showDesc(event) {
    var buttonPressed = $(event.target);
    var capLongDesc = buttonPressed.nextAll('.cixblockLongDesc');
    capLongDesc.slideToggle(100, function() {
        if (capLongDesc.is(":hidden")) {
            buttonPressed.text("Show long description");
            buttonPressed.attr("aria-expanded", "false");
        } else {
            buttonPressed.text("Hide long description");
            buttonPressed.attr("aria-expanded", "true");
        }
    });
}
