"""A simple xblock for displaying images"""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, String
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioEditableXBlockMixin

class CaptionedImageXBlock(StudioEditableXBlockMixin, XBlock):
    """
    A simple xblock to make images neater and have captions with long descriptions and copyright acknowledgments.
    """ 

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.
    display_name = String(display_name="Display name", default='Image')
    template = String(display_name="Style", default="1", scope=Scope.content, values=('1', '2'),
        help="Template 1 is suitable for images 910px wide or larger. Template 2 is suitable for images 640px wide or larger. Portrait images should use template 2, while landscape works with either. Please note that if your image is too small, it will be enlarged for potentially poor quality results.")
    imageURL = String(display_name="Image URL", default="", scope=Scope.content,
        help="Enter the URL of your image.")
    caption = String(display_name="Caption", multiline_editor='html', resettable_editor=False,
        default="", scope=Scope.content,
        help="Enter your image caption. Example: Figure 2 - The Eiffel Tower")
    attribution = String(display_name="Attribution", multiline_editor='html', resettable_editor=False,
        default="", scope=Scope.content,
        help="Enter the copyright holder or other attribution for the image.")
    longDesc = String(display_name="Long description text", multiline_editor='html', resettable_editor=False,
        default="", scope=Scope.content,
        help="Enter a long description of your image here. This will be visible to all users. Do not repeat the contents of your caption, instead describe the image as you would to someone else over the phone.")

    # Make fields editable in studio
    editable_fields = ('display_name', 'imageURL', 'caption', 'attribution', 'longDescription', )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        html = self.resource_string("static/html/captionedimage.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/captionedimage.css"))
        frag.add_javascript(self.resource_string("static/js/src/captionedimage.js"))
        frag.initialize_js('PrintXBlock')
        return frag
