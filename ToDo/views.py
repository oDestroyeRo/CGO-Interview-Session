from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(["GET"])
def assignment(request):
    X = int(request.query_params.get('X'))
    A = request.query_params.get('A')
    A = list(map(int, A))
    content = {"result": solution(X,A)}
    return JsonResponse(content)



def solution(X,A):
    position = [False for i in range(X+1)]
    for i in range(len(A)):
        if(not position[A[i]]):
            X = X - 1
            position[A[i]] = True
        if (X == 0):
            return i
    return -1