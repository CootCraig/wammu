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
Contact and phone number select dialogs
'''

import wx
import Wammu.Utils
from Wammu.Utils import StrConv, Str_ as _

def SortName(i1, i2):
    return cmp(i1['Name'], i2['Name'])

def SelectContact(parent, list, index = False):
    list.sort(SortName)
    choices = []
    for e in list:
        choices.append(StrConv(e['Name']))

    dlg = wx.SingleChoiceDialog(parent, _('Select contact from bellow list'), _('Select contact'),
                                choices, wx.CHOICEDLG_STYLE | wx.RESIZE_BORDER)
    if dlg.ShowModal() == wx.ID_OK and len(choices) > 0:
        rs = dlg.GetSelection()
        if not index:
            rs =  list[rs]['Location']
    else:
        rs = -1
    del dlg
    return rs

def SelectNumber(parent, list):
    i = SelectContact(parent, list, True)
    if i == -1:
        return None
    return SelectContactNumber(parent, list[i])

def SelectContactNumber(parent, item):
    numbers = []
    texts = []
    for x in range(len(item['Entries'])):
        if Wammu.Utils.GetItemType(item['Entries'][x]['Type']) == 'phone':
            numbers.append(item['Entries'][x]['Value'])
            texts.append(StrConv(item['Entries'][x]['Type'] + ' : ' + item['Entries'][x]['Value']))

    if len(numbers) == 0:
        return None
    elif len(numbers) == 1:
        return numbers[0]
    dlg = wx.SingleChoiceDialog(parent, _('Select number for selected contact'), _('Select phone number'),
                                texts, wx.CHOICEDLG_STYLE | wx.RESIZE_BORDER)
    if dlg.ShowModal() == wx.ID_OK:
        rs = numbers[dlg.GetSelection()]
    else:
        rs = None
    del dlg
    return rs
