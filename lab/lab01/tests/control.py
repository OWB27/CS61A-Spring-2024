test = {
  'name': 'Control',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def xk(c, d):
          ...     if c == 4:
          ...         return 6
          ...     elif d >= 4:
          ...         return 6 + 7 + c
          ...     else:
          ...         return 25
          >>> xk(10, 10)
          23
          >>> xk(10, 6)
          23
          >>> xk(4, 6)
          6
          >>> xk(0, 0)
          25
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> def how_big(x):
          ...     if x > 10:
          ...         print('huge')
          ...     elif x > 5:
          ...         return 'big'
          ...     if x > 0:
          ...         print('positive')
          ...     else:
          ...         print(0)
          >>> how_big(7)  # Be careful with quotation marks!
          'big'
          >>> print(how_big(7))  # Be careful with quotation marks!
          big
          >>> how_big(12)
          huge
          positive
          >>> print(how_big(12))
          huge
          positive
          None
          >>> print(how_big(1), how_big(0))
          98a026fcc10e24150ac1d08bf0cde5a9
          b0754f6baafe74512d1be0bd5c8098ed
          342c92c77f6ac0d470d055412adc2e0e
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> n = 3
          >>> while n >= 0:  # If this loops forever, just type Infinite Loop
          ...     n -= 1
          ...     print(n)
          6d6f378f0affa7f84aa38e519e353617
          f26f9ec9ba426ebfdd8a43b22c8c74a0
          b0754f6baafe74512d1be0bd5c8098ed
          8e8a6ea9b75e03aef4652f8a6bc37fba
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': True
        },
        {
          'code': r"""
          >>> negative = -12
          >>> while negative: # If this loops forever, just type Infinite Loop
          ...    if negative + 6:
          ...        print(negative)
          ...    negative += 3
          b3c9c48be5cbc9295c81c3e75d1538d8
          efbd765b468a29852de43786a3d7f2b9
          065654bed198eae1187f5223b6973a0c
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
