from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class ThrottleRate(UserRateThrottle):
    scope = 'jack'