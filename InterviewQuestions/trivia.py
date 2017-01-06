# About JD
# - interesting technical problem
#   * Wells - colleague was spending 2 weeks simply collecting data for her quarterly analytics reports.
#     I automated via SqlTemplate mechanism from 2 weeks down to 2 hours.
#   * YP - 45 join query and make it performant (and accurate)
# - interpersonal conflict
#   * Colleague was too busy to help me understand how a previously working process of grabbing csv's from ftp site
#     was working.  I knew that it was probably backed up, and talked to couple of managers to find the right systems
#     engineer to restore the lost filesystem and recover her code so I could stop bothering her and simply read
#     the code myself to understand the prior working process (which was now breaking and needing fixing).
# - leadership or ownership
#   * Multiple times throughout career.  Examples, YP and changing data pipelines + tools used for data analytics
#     Wells - noticed lots of tedious double work happening across spreadsheets for Systems Architecture group.  Despite
#     not being my job, I couldn't stand the tedious work myself, so I spent weekend writing a better spreadsheet system
#     which made references across sheets to lower copy/paste.  This made it much faster to do project estimations
#     and eventually won over entire team to using my new spreadsheet system which was superior to the old clunky one.
# - done differently in a past project
#   * Sqor - should have iterated faster cause startup wanted to see results within week or two always.  Sometimes some
#     problems shouldn't be tried to solve with correct design base but simply just smaller evolutionary changes from
#     existing codebase.  Was a tough environment though and ultimately was led by bad CTO leadership IMO.  CTO has
#     since left the company after I left.
#
# Questions from JD:
# - re: company's product/business
#   * how is your company lean and mean as an organization?
#   * biggest current business/engineering challenges?
#   * how does your company maintain the moat - competitive advantage over competition?
# - re: engineering strategy
#   * test driven design?  scrum?


def trivia():
    s = PythonTrivia()
    print("s.bar = {}".format(s.get_bar()))
    return True


class PythonTrivia:
    def __init__(foo):
        print("Note __init__ uses 'foo' arg as setting its internal bar attribute and "
              "the get_bar uses the standard 'self' arg")
        print()
        foo.bar = "Python trivia:  Class' use of self arg within methods is simply a naming convention.."

    def get_bar(self):
        return self.bar
