from .models import Claim, Comment
from .forms import ClaimForm, CommentForm


class ClaimMixin:
    template_name = 'employment_portfolio/claim/create.html'
    model = Claim
    context_object_name = "claims"


class ClaimEditMixin:
    form_class = ClaimForm


class CommentMixin:
    template_name = 'employment_portfolio/comment/create.html'
    model = Comment
    context_object_name = "comments"


class CommentEditMixin:
    form_class = CommentForm

