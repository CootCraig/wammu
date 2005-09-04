# -*- coding: UTF-8 -*-
# Wammu - Phone manager
# Copyright (c) 2003 - 2005 Michal Čihař
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
'''
Some static data, bitmaps, etc.
'''

import sys
from Wammu.Utils import Str_ as _

# When support for sound will be implemented, here should be sounds
PredefinedSounds = [
        (_('Chimes high'),''),
        (_('Chimes low'),''),
        (_('Ding'),''),
        (_('TaDa'),''),
        (_('Notify'),''),
        (_('Drum'),''),
        (_('Claps'),''),
        (_('Fanfare'),''),
        (_('Chord high'),''),
        (_('Chord low'),''),
        ]

# Wanted somebody who will draw nicer icons :-)

Note = [
    '16 16 2 1',
    'x c Black',
    '  c None',
    '      xx        ',
    '      xxx  xxx  ',
    '      xxxxxxxxx ',
    '      xx  xx  xx',
    '      xx        ',
    '      xx        ',
    '      xx        ',
    '      xx        ',
    '  xxxxxx        ',
    ' xxxxxxx        ',
    'xxxxxxxx        ',
    'xxxxxxxx        ',
    'x  xxxxx        ',
    'x   xxxx        ',
    ' x  xxx         ',
    '  xxxx          ']

UnknownPredefined = [
    '16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '    x      x    ',
    '   x  xxxx  x   ',
    '   x x    x x   ',
    '    x     x x   ',
    '          x x   ',
    '         x x    ',
    '        x x     ',
    '       x x      ',
    '       x x      ',
    '       xx       ',
    '                ',
    '       xx       ',
    '      xxxx      ',
    '      x xx      ',
    '       xx       ']

PredefinedAnimations = [
    (_("I'm ironic, flirty"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '   xx      xx   ',
    '  x          x  ',
    ' x            x ',
    ' x  xx   xx   x ',
    'x   x x  x x   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x              x',
    'x   x      x   x',
    ' x   x    x   x ',
    ' x    x  x    x ',
    '  x    xx    x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("I am glad"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '   xx      xx   ',
    '  x          x  ',
    ' x            x ',
    ' x  xx   xx   x ',
    'x   x x  x x   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x              x',
    'x   x      x   x',
    ' x   x    x   x ',
    ' x    xxxx    x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("I am skeptic"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '   xx      xx   ',
    '  x          x  ',
    ' x            x ',
    ' x  xx   xx   x ',
    'x   x x  x x   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x              x',
    'x   xxxxx      x',
    ' x       x    x ',
    ' x        x   x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("I am sad"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '   xx      xx   ',
    '  x          x  ',
    ' x            x ',
    ' x  xx   xx   x ',
    'x   x x  x x   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x              x',
    'x     xxxx     x',
    ' x   x    x   x ',
    ' x  x      x  x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("WOW"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '   xx      xx   ',
    '  x          x  ',
    ' x            x ',
    ' x  xx   xx   x ',
    'x   x x  x x   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x     xxxx     x',
    'x    x    x    x',
    ' x   x    x   x ',
    ' x    xxxx    x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("I am crying"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '   xx      xx   ',
    '  x          x  ',
    ' x            x ',
    ' x  xx   xx   x ',
    'x   x x  x x   x',
    'x    xx   xx   x',
    'x     x    x   x',
    'x              x',
    'x              x',
    'x     xxxx     x',
    ' x   x    x   x ',
    ' x    xxxx    x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("I am winking"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '   xx      xx   ',
    '  x          x  ',
    ' x            x ',
    ' x       xx   x ',
    'x  xxxx  x x   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x              x',
    'x   x      x   x',
    ' x   xxxxxx   x ',
    ' x            x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("I am laughing"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '   xx      xx   ',
    '  x          x  ',
    ' x            x ',
    ' x  xx   xx   x ',
    'x   x x  x x   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x              x',
    'x   x      x   x',
    ' x   xxxxxx   x ',
    ' x    xxxx    x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("I am indifferent"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '   xx      xx   ',
    '  x          x  ',
    ' x            x ',
    ' x  xx   xx   x ',
    'x   x x  x x   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x              x',
    'x              x',
    ' x            x ',
    ' x   xxxxxx   x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("I am in love"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxx xx xx ',
    '   xx    x  x  x',
    '  x       x   x ',
    ' x         x x  ',
    ' x  xx   xx x x ',
    'x   x x  x x   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x              x',
    'x              x',
    ' x   x    x   x ',
    ' x    xxxx    x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("I am confused"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx xx  ',
    '   xx      x  x ',
    '  x           x ',
    ' x           x  ',
    ' x  xx   xx    x',
    'x   x x  x x x x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x              x',
    'x              x',
    ' x   xxxxx    x ',
    ' x            x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("Tongue hanging out"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '   xx      xx   ',
    '  x          x  ',
    ' x            x ',
    ' x  xx   xx   x ',
    'x   x x  x x   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x              x',
    'x              x',
    ' x         x  x ',
    ' x    xxxxx x x ',
    '  x     xx   x  ',
    '   xx     x   x ',
    '     xxxxxxxxx  ']),
    (_("I am angry"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '   xx      xx   ',
    '  x          x  ',
    ' x x        x x ',
    ' x  xx   xxx  x ',
    'x   x x  x x   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x              x',
    'x     xxxx     x',
    ' x   x    x   x ',
    ' x  x      x  x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("Wearing glases"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '   xx      xx   ',
    '  x          x  ',
    ' x            x ',
    'xxxxxxxxxxxxxxxx',
    'x   xxx  xxx   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x              x',
    'x              x',
    ' x  x      x  x ',
    ' x   xxxxxx   x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("Devil"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    'x    xxxxxx    x',
    'xxxxx      xxxxx',
    ' xx          xx ',
    ' x            x ',
    ' x  xx   xx   x ',
    'x   x x  x x   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x   xxxxxxxx   x',
    'x   x x  x x   x',
    ' x   x    x   x ',
    ' x    xxxx    x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    ]

# FIXME: these definitions probably should be part of gammu module and not this...
# First is used as default
Models = [
    'auto',
    'at',
    'alcatel',
    'nauto',
    'obex',
    'seobex',
    ]
Connections = [
    'at19200',
    'at115200',
    'fbus',
    'fbusirda',
    'fbusdlr3',
    'fbusdku5',
    'mbus',
    'irdaphonet',
    'irdaat',
    'irdaobex',
    'dku2phonet',
    'dku5fbus2',
    'bluerffbus',
    'bluerfphonet',
    'bluephonet',
    'bluerfat',
    'blueat',
    ]

Conn_Cable = [
    'at19200',
    'fbusdlr3',
    'fbus',
    'mbus',
    ]
Conn_IrDA_Win = [
    'irdaphonet',
    ]
Conn_IrDA_Other = [
    'irdaphonet',
    'at19200',
    ]
Conn_Bluetooth = [
    'bluephonet',
    'blueat',
    'bluerfat',
    'bluerffbus',
    'bluerfphonet',
    ]
if sys.platform == 'win32':
    Devices = [
        'com1:',
        'com2:',
        ]
    AllDevices = [
        (Conn_IrDA_Win, '', None),
        (Conn_Cable, 'com%d:', (1,4)),
        ]
# FIXME: support more platforms?
else:
    Devices = [
        '/dev/ttyS0',
        '/dev/ttyS1',
        '/dev/ttyUSB0',
        '/dev/ttyUSB1',
        '/dev/ttyACM0',
        '/dev/ttyACM1',
        '/dev/ircomm0',
        '/dev/usb/tts/0',
        ]
    AllDevices = [
        (Conn_Cable, '/dev/ttyS%d', (0, 3)),
        (Conn_Cable, '/dev/ttyUSB%d', (0, 3)),
        (Conn_Cable, '/dev/ttyACM%d', (0, 3)),
        (Conn_IrDA_Other, '/dev/ircomm%d', (0, 1)),
        (Conn_Cable, '/dev/usb/tts/%d', (0, 3)),
        ]

ContactMemoryTypes = ['ME', 'SM']

SMSIDs = {
    'Text':                 [
        'Text',
        'ConcatenatedTextLong',
        'ConcatenatedAutoTextLong',
        'ConcatenatedTextLong16bit',
        'ConcatenatedAutoTextLong16bit',
        ],
    'Sound':                [
        'NokiaProfileLong',
        'NokiaRingtone',
        'NokiaRingtoneLong',
        'EMSSound10',
        'EMSSound12',
        'EMSSonyEricssonSound',
        'EMSSound10Long',
        'EMSSound12Long',
        'EMSSonyEricssonSoundLong',
        ],
    'Animation':            [
        'NokiaProfileLong',
        'EMSAnimation',
        'AlcatelMonoAnimationLong',
        'NokiaScreenSaverLong',
        ],
    'Bitmap':               [
        'NokiaProfileLong',
        'NokiaPictureImageLong',
        'NokiaOperatorLogo',
        'NokiaOperatorLogoLong',
        'NokiaCallerLogo',
        'EMSFixedBitmap',
        'EMSVariableBitmap',
        'EMSVariableBitmapLong',
        'AlcatelMonoBitmapLong',
        'AlcatelSMSTemplateName',
        ],
    'PredefinedAnimation':  [
        'EMSPredefinedAnimation',
        ],
    'PredefinedSound':      [
        'EMSPredefinedSound',
        ],
    }



MemoryValueTypes = [
    'Number_General',
    'Number_Mobile',
    'Number_Work',
    'Number_Fax',
    'Number_Home',
    'Number_Pager',
    'Number_Other',
    'Text_Note',
    'Text_Postal',
    'Text_Email',
    'Text_Email2',
    'Text_URL',
    'Date',
    'Caller_Group',
    'Text_Name',
    'Text_LastName',
    'Text_FirstName',
    'Text_Company',
    'Text_JobTitle',
    'Category',
    'Private',
    'Text_StreetAddress',
    'Text_City',
    'Text_State',
    'Text_Zip',
    'Text_Country',
    'Text_Custom1',
    'Text_Custom2',
    'Text_Custom3',
    'Text_Custom4',
    'Text_UserID',
    'RingtoneID',
    'RingtoneFileSystemID',
    'PictureID',
    'SMSListID',
    ]

CalendarTypes = [
    'REMINDER',
    'CALL',
    'MEETING',
    'BIRTHDAY',
    'MEMO',
    'TRAVEL',
    'VACATION',
    'T_ATHL',
    'T_BALL',
    'T_CYCL',
    'T_BUDO',
    'T_DANC',
    'T_EXTR',
    'T_FOOT',
    'T_GOLF',
    'T_GYM',
    'T_HORS',
    'T_HOCK',
    'T_RACE',
    'T_RUGB',
    'T_SAIL',
    'T_STRE',
    'T_SWIM',
    'T_TENN',
    'T_TRAV',
    'T_WINT',
    'ALARM',
    'DAILY_ALARM',
    ]

CalendarValueTypes = [
    'START_DATETIME',
    'END_DATETIME',
    'ALARM_DATETIME',
    'SILENT_ALARM_DATETIME',
    'RECURRANCE',
    'TEXT',
    'LOCATION',
    'PHONE',
    'PRIVATE',
    'CONTACTID',
    'REPEAT_DAYOFWEEK',
    'REPEAT_DAY',
    'REPEAT_WEEKOFMONTH',
    'REPEAT_MONTH',
    'REPEAT_FREQUENCY',
    'REPEAT_STARTDATE',
    'REPEAT_STOPDATE',
    ]

TodoPriorities = [
    'High',
    'Medium',
    'Low',
    ]

TodoValueTypes = [
    'END_DATETIME',
    'COMPLETED',
    'ALARM_DATETIME',
    'SILENT_ALARM_DATETIME',
    'TEXT',
    'PRIVATE',
    'CATEGORY',
    'CONTACTID',
    'PHONE',
    ]

TextFormats = [
    [(_('Alignment'), _('None')),
        ('Left', _('Left'), '<div align="left">%s</div>'),
        ('Right', _('Right'), '<div align="right">%s</div>'),
        ('Center', _('Center'), '<div align="center">%s</div>'),
        ],
    [(_('Text Size'), _('Normal')),
        ('Large', _('Large'), '<font size="+2">%s</font>'),
        ('Small', _('Small'), '<font size="-2">%s</font>'),
        ],
    ['', ('Bold', _('Bold'), '<b>%s</b>')],
    ['', ('Italic', _('Italic'), '<i>%s</i>')],
    ['', ('Underlined', _('Underlined'), '<u>%s</u>')],
    ['', ('Strikethrough', _('Strikethrough'), '<strike>%s</strike>')],
]


