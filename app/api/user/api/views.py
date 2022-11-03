from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class UserView(ListCreateAPIView):
    serializer_class = None
    permission_classes = []

    def get_queryset(self):
        pass

    def create(self, request, *args, **kwargs):
        pass


class UserDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = None
    permission_classes = []

    def get_object(self):
        pass

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass
