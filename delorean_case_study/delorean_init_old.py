from delorean_case_study.bii_server_1_scaffolding import *
from delorean_case_study.environment import *

############################################### 
# DELOREAN CODE (LIBRARY)
###############################################

class Delorean(object):
    """
    The class `Delorean <Delorean>` object. This method accepts naive
    datetime objects, with a string timezone.
    """
    _VALID_SHIFT_DIRECTIONS = ('last', 'next')
    _VALID_SHIFT_UNITS = ('second', 'minute', 'hour', 'day', 'week',
                          'month', 'year', 'monday', 'tuesday', 'wednesday',
                          'thursday', 'friday', 'saturday', 'sunday')

    def __init__(self, datetime=None, timezone=None):
        # maybe set timezone on the way in here. if here set it if not
        # use UTC
        is_datetime_instance(datetime)

        if datetime:
            if is_datetime_naive(datetime):
                if timezone:
                    if isinstance(timezone, tzoffset):
                        utcoffset = timezone.utcoffset(None)
                        total_seconds = (
                            (utcoffset.microseconds + (
                                utcoffset.seconds + utcoffset.days * 24 * 3600) * 10 ** 6) / 10 ** 6)
                        self._tzinfo = pytz.FixedOffset(total_seconds / 60)
                    elif isinstance(timezone, tzinfo):
                        self._tzinfo = timezone
                    else:
                        self._tzinfo = pytz.timezone(timezone)
                    self._dt = localize(datetime, self._tzinfo)
                else:
                    # TODO(mlew, 2015-08-09):
                    # Should we really throw an error here, or should this 
                    # default to UTC?)
                    # raise DeloreanInvalidTimezone('Provide a valid timezone')
                    raise ValueError('Provide a valid timezone')
            else:
                self._tzinfo = datetime.tzinfo
                self._dt = datetime
        else:
            if timezone:
                if isinstance(timezone, tzoffset):
                    self._tzinfo = pytz.FixedOffset(timezone.utcoffset(None).total_seconds() / 60)
                elif isinstance(timezone, tzinfo):
                    self._tzinfo = timezone
                else:
                    self._tzinfo = pytz.timezone(timezone)

                self._dt = datetime_timezone(self._tzinfo)
                self._tzinfo = self._dt.tzinfo
            else:
                self._tzinfo = pytz.utc
                self._dt = datetime_timezone('UTC')

    def shift(self, timezone):
        """
        Shifts the timezone from the current timezone to the specified timezone associated with the Delorean object,
        modifying the Delorean object and returning the modified object.
        .. testsetup::
            from datetime import datetime
            from delorean import Delorean
        .. doctest::
            >>> d = Delorean(datetime(2015, 1, 1), timezone='US/Pacific')
            >>> d.shift('UTC')
            Delorean(datetime=datetime.datetime(2015, 1, 1, 8, 0), timezone='UTC')
        """
        try:
            self._tzinfo = pytz.timezone(timezone)
        ## except pytz.UnknownTimeZoneError:
        except Exception:
            raise DeloreanInvalidTimezone('Provide a valid timezone')
        self._dt = self._tzinfo.normalize(self._dt.astimezone(self._tzinfo))
        self._tzinfo = self._dt.tzinfo
        return self

    def truncate(self, s):
        """
        Truncate the delorian object to the nearest s
        (second, minute, hour, day, month, year)

        This is a destructive method, modifies the internal datetime
        object associated with the Delorean object.

        .. testsetup::

            from datetime import datetime
            from delorean import Delorean

        .. doctest::

            >>> d = Delorean(datetime(2015, 1, 1, 12, 10), timezone='US/Pacific')
            >>> d.truncate('hour')
            Delorean(datetime=datetime.datetime(2015, 1, 1, 12, 0), timezone='US/Pacific')

        """
        # if s == 'second': 
        #     self._dt = self._dt.replace(microsecond=0)
        # elif s == 'minute':
        #     self._dt = self._dt.replace(second=0, microsecond=0)
        # elif s == 'hour':
        #     self._dt = self._dt.replace(minute=0, second=0, microsecond=0)
        # elif s == 'day':
        #     self._dt = self._dt.replace(hour=0, minute=0, second=0, microsecond=0)
        # elif s == 'month':
        #     self._dt = self._dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        # elif s == 'year':
        #     self._dt = self._dt.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
        # else:
        #     raise ValueError("Invalid truncation level")

        pass

    @property
    def epoch(self):
        """
        Returns the total seconds since epoch associated with
        the Delorean object.

        .. testsetup::

            from datetime import datetime
            from delorean import Delorean

        .. doctest::

            >>> d = Delorean(datetime(2015, 1, 1), timezone='US/Pacific')
            >>> d.epoch
            1420099200.0

        """
        # epoch_sec = pytz.utc.localize(datetime.utcfromtimestamp(0))
        # now_sec = pytz.utc.normalize(self._dt)
        # delta_sec = now_sec - epoch_sec
        # return get_total_second(delta_sec)
        return self._dt.epoch