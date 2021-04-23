#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 17:25:00 2019

@author: sambhav
"""
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from user.serializers import UserRegistrationSerializer
from profile.models import UserProfile
import json


class UserProfileView(RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            print('user profile when onluy fetching the profile', request.user, user_profile.first_name)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User profile fetched successfully',
                'data': {
                    'user_id': user_profile.id,
                    'email': user_profile.user.email,
                    'first_name': user_profile.first_name,
                    'last_name': user_profile.last_name,
                    'phone_number': user_profile.phone_number,
                    'address': user_profile.address,
                    }
                }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'User does not exists',
                'error': str(e)
                }
        return Response(response, status=status_code)

    def put(self, request):
        # curl --location --request PUT http://localhost:8000/api/profile -H 'Content-Type: application/json' --data-raw '@updated_info.json' --header 'Authorization: Bearer JWTToken.....................'

        status_code  = status.HTTP_200_OK
        payload      = json.loads(request.body)
        print("pay sent in request.body is : ", payload)
        try:
            user_profile = UserProfile.objects.filter(user=request.user)
            print(request.user, " is the request user")
            print("user profile is " , user_profile)
            print(user_profile.first().first_name)
        except:
            response={
                    'success': 'false',
                    'status code': status.HTTP_400_BAD_REQUEST,
                    'message': 'User does not exists',
                    'error': str(e)
                    }
        else:
            user_profile.update(**payload)
            print("after update : ", user_profile.first().first_name)
            # curl PUT http://localhost:8000/profile '@put_json' -H 'Content-Type: application/json' --header 'Authorization : Bearer ....'
            response = {
                    'success': 'true',
                    'status code': status_code,
                    'message': 'User profile updated successfully',
                    'data': {
                        'first_name': user_profile.first().first_name,
                        'last_name': user_profile.first().last_name,
                        'phone_number': user_profile.first().phone_number,
                        'address': user_profile.first().address,
                        'email': user_profile.first().user.email
                        }
                    }
        return Response(response, status=status_code)
