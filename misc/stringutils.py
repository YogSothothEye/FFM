"""
    FFM by @JusticeRage

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


def find_last_of(s, chars):
    """
    Finds the last instance of a char from the given group in a string.
    :param s: The string to search.
    :param chars: The group of characters to look for.
    :return: The index of the character in the string, or -1.
    """
    for i in range(0, len(s)):
        index = len(s) - i - 1
        if s[len(s) - i - 1] in chars:
            return index
    return -1
