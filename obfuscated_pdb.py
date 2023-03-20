import os as _3ba43
import io as _91d42
import re as _b1457
import sys as _0c902
import cmd as _feba2
import bdb as _94215
import dis as _c7221
import code as _bddd9
import glob as _62b74
import pprint as _d959d
import signal as _3610b
import inspect as _16436
import tokenize as _d5c74
import functools as _b36e2
import traceback as _df75f
import linecache as _7c5e6
from typing import Union as _0fe95

class Restart(Exception):
    """Causes a debugger to be restarted for the debugged python program."""
    pass
__all__ = ['run', 'pm', 'Pdb', 'runeval', 'runctx', 'runcall', 'set_trace', 'post_mortem', 'help']

def _cfbec(_29d12, _a30b9):
    _6e425 = _b1457('def\\s+%s\\s*[(]' % _b1457(_29d12))
    try:
        _283e6 = _d5c74(_a30b9)
    except OSError:
        return None
    with _283e6:
        for (_f91cc, _4ab90) in enumerate(_283e6, start=1):
            if _6e425(_4ab90):
                return (_29d12, _a30b9, _f91cc)
    return None

def _a0fde(_bddd9, _377ee):
    _b97be = list(_c7221(_bddd9))
    _b97be()
    for (_8830d, _f91cc) in _b97be:
        if _377ee >= _8830d:
            return _f91cc
    return 0

class _rstr(str):
    """String that doesn't quote its repr."""

    def _c0786(_928cf):
        return _928cf

class _ScriptTarget(str):

    def _b6ae3(_5ead7, _60a39):
        _aba42 = super()(_5ead7, _3ba43(_60a39))
        _aba42 = _60a39
        return _aba42

    def _03f70(_928cf):
        if not _3ba43(_928cf):
            print('Error:', _928cf, 'does not exist')
            _0c902(1)
        _0c902[0] = _3ba43(_928cf)

    @property
    def _a30b9(_928cf):
        return _928cf

    @property
    def _8c7bf(_928cf):
        return dict(__name__='__main__', __file__=_928cf, __builtins__=__builtins__)

    @property
    def _bddd9(_928cf):
        with _91d42(_928cf) as _283e6:
            return f"exec(compile({_283e6()!r}, {_928cf!r}, 'exec'))"

class _ModuleTarget(str):

    def _03f70(_928cf):
        try:
            _928cf
        except Exception:
            _df75f()
            _0c902(1)

    @_b36e2.cached_property
    def _03f13(_928cf):
        import runpy as _b8223
        return _b8223(_928cf)

    @property
    def _a30b9(_928cf):
        return _928cf

    @property
    def _bddd9(_928cf):
        (_647b9, _ea73b, _bddd9) = _928cf
        return _bddd9

    @property
    def _a8870(_928cf):
        (_647b9, _ea73b, _bddd9) = _928cf
        return _ea73b

    @property
    def _8c7bf(_928cf):
        return dict(__name__='__main__', __file__=_3ba43(_3ba43(_928cf)), __package__=_928cf, __loader__=_928cf, __spec__=_928cf, __builtins__=__builtins__)
_7bf3a = '\n-> '

class Pdb(_94215, _feba2):
    _d7e19 = None

    def _3a1ff(_928cf, _bfb18='tab', _3ecc3=None, _98107=None, _0b679=None, _dbbfe=False, _1906e=True):
        _94215(_928cf, skip=_0b679)
        _feba2(_928cf, _bfb18, _3ecc3, _98107)
        _0c902('pdb.Pdb')
        if _98107:
            _928cf = 0
        _928cf = '(Pdb) '
        _928cf = {}
        _928cf = {}
        _928cf = ''
        _928cf = False
        _928cf = {}
        try:
            import readline as _aedc0
            _aedc0(' \t\n`@#$%^&*()=+[{]}\\|;:\'",<>?')
        except ImportError:
            pass
        _928cf = False
        _928cf = _dbbfe
        _928cf = []
        if _1906e:
            try:
                with open(_3ba43('~/.pdbrc'), encoding='utf-8') as _6f09c:
                    _928cf(_6f09c)
            except OSError:
                pass
            try:
                with open('.pdbrc', encoding='utf-8') as _6f09c:
                    _928cf(_6f09c)
            except OSError:
                pass
        _928cf = {}
        _928cf = {}
        _928cf = {}
        _928cf = False
        _928cf = None

    def _cb733(_928cf, _e1381, _b7a43):
        if _928cf:
            raise KeyboardInterrupt
        _928cf("\nProgram interrupted. (Use 'cont' to resume).")
        _928cf()
        _928cf(_b7a43)

    def _bba04(_928cf):
        _94215(_928cf)
        _928cf()

    def _264be(_928cf):
        _928cf = None
        _928cf = []
        _928cf = 0
        _928cf = None
        _928cf()

    def _e8146(_928cf, _d796e, _ba267):
        _928cf()
        (_928cf, _928cf) = _928cf(_d796e, _ba267)
        while _ba267:
            _f91cc = _a0fde(_ba267, _ba267)
            _928cf[_ba267] = _f91cc
            _ba267 = _ba267
        _928cf = _928cf[_928cf][0]
        _928cf = _928cf
        return _928cf()

    def _16dbc(_928cf):
        if not _928cf:
            return
        _5fea2 = _928cf
        _5fea2()
        _928cf = []
        while _5fea2:
            _4ab90 = _5fea2()()
            if _4ab90 and _4ab90[0] != '#':
                if _928cf(_4ab90):
                    _928cf += reversed(_5fea2)
                    return True

    def _d25b5(_928cf, _b7a43, _51d50):
        """This method is called when there is the remote possibility
        that we ever need to stop in this function."""
        if _928cf:
            return
        if _928cf(_b7a43):
            _928cf('--Call--')
            _928cf(_b7a43, None)

    def _bafa3(_928cf, _b7a43):
        """This function is called when we stop or break at this line."""
        if _928cf:
            if _928cf != _928cf(_b7a43) or _b7a43 <= 0:
                return
            _928cf = False
        if _928cf(_b7a43):
            _928cf(_b7a43, None)

    def _252d8(_928cf, _b7a43):
        """Call every command that was set for the current active breakpoint
        (if there is one).

        Returns True if the normal interaction function must be called,
        False otherwise."""
        if getattr(_928cf, 'currentbp', False) and _928cf in _928cf:
            _9698f = _928cf
            _928cf = 0
            _7e60f = _928cf
            _928cf(_b7a43, None)
            for _4ab90 in _928cf[_9698f]:
                _928cf(_4ab90)
            _928cf = _7e60f
            if not _928cf[_9698f]:
                _928cf(_928cf[_928cf])
            if _928cf[_9698f]:
                _928cf()
            _928cf()
            return
        return 1

    def _408b3(_928cf, _b7a43, _b0cfb):
        """This function is called when a return trap is set here."""
        if _928cf:
            return
        _b7a43['__return__'] = _b0cfb
        _928cf('--Return--')
        _928cf(_b7a43, None)

    def _ee6d9(_928cf, _b7a43, _ab41d):
        """This function is called if an exception occurs,
        but only if we are to stop at or just below this level."""
        if _928cf:
            return
        (_2f807, _68185, _85bd9) = _ab41d
        _b7a43['__exception__'] = (_2f807, _68185)
        _574f2 = 'Internal ' if not _85bd9 and _2f807 is StopIteration else ''
        _928cf('%s%s' % (_574f2, _df75f(_2f807, _68185)[-1]()))
        _928cf(_b7a43, _85bd9)

    def _0a185(_928cf):
        while True:
            try:
                _928cf = True
                _928cf()
                _928cf = False
                break
            except KeyboardInterrupt:
                _928cf('--KeyboardInterrupt--')

    def _32861(_928cf):
        _db198 = _928cf(_928cf)
        if _db198:
            for (_23fea, _e915e) in _db198():
                _261fa = _928cf(_23fea)
                if _261fa is not _e915e and _261fa != _e915e:
                    _db198[_23fea] = _261fa
                    _928cf('display %s: %r  [old: %r]' % (_23fea, _261fa, _e915e))

    def _53446(_928cf, _b7a43, _df75f):
        if _43e42:
            try:
                _3610b(_3610b, _43e42)
            except ValueError:
                pass
            else:
                _43e42 = None
        if _928cf(_b7a43, _df75f):
            _928cf()
            return
        _928cf(_928cf[_928cf])
        _928cf()
        _928cf()

    def _52b0b(_928cf, _7e390):
        """Custom displayhook for the exec in default(), which prevents
        assignment of the _ variable in the builtins.
        """
        if _7e390 is not None:
            _928cf(repr(_7e390))

    def _0dec5(_928cf, _4ab90):
        if _4ab90[:1] == '!':
            _4ab90 = _4ab90[1:]
        locals = _928cf
        globals = _928cf
        try:
            _bddd9 = compile(_4ab90 + '\n', '<stdin>', 'single')
            _ccd13 = _0c902
            _d9866 = _0c902
            _580cc = _0c902
            try:
                _0c902 = _928cf
                _0c902 = _928cf
                _0c902 = _928cf
                exec(_bddd9, globals, locals)
            finally:
                _0c902 = _ccd13
                _0c902 = _d9866
                _0c902 = _580cc
        except:
            _928cf()

    def _9f74e(_928cf, _4ab90):
        """Handle alias expansion and ';;' separator."""
        if not _4ab90():
            return _4ab90
        _0ad6b = _4ab90()
        while _0ad6b[0] in _928cf:
            _4ab90 = _928cf[_0ad6b[0]]
            _3f770 = 1
            for _e6e87 in _0ad6b[1:]:
                _4ab90 = _4ab90('%' + str(_3f770), _e6e87)
                _3f770 += 1
            _4ab90 = _4ab90('%*', ' '(_0ad6b[1:]))
            _0ad6b = _4ab90()
        if _0ad6b[0] != 'alias':
            _d293f = _4ab90(';;')
            if _d293f >= 0:
                next = _4ab90[_d293f + 2:]()
                _928cf(next)
                _4ab90 = _4ab90[:_d293f]()
        return _4ab90

    def _d1ef9(_928cf, _4ab90):
        """Interpret the argument as though it had been typed in response
        to the prompt.

        Checks whether this line is typed at the normal prompt or in
        a breakpoint command list definition.
        """
        if not _928cf:
            return _feba2(_928cf, _4ab90)
        else:
            return _928cf(_4ab90)

    def _1187c(_928cf, _4ab90):
        """Handles one command line during command list definition."""
        (_feba2, _95501, _4ab90) = _928cf(_4ab90)
        if not _feba2:
            return
        if _feba2 == 'silent':
            _928cf[_928cf] = True
            return
        elif _feba2 == 'end':
            _928cf = []
            return 1
        _e1149 = _928cf[_928cf]
        if _95501:
            _e1149(_feba2 + ' ' + _95501)
        else:
            _e1149(_feba2)
        try:
            _b96aa = getattr(_928cf, 'do_' + _feba2)
        except AttributeError:
            _b96aa = _928cf
        if _b96aa in _928cf:
            _928cf[_928cf] = False
            _928cf = []
            return 1
        return

    def _db0ff(_928cf, _10f30):
        print(_10f30, file=_928cf)

    def _f1c64(_928cf, _10f30):
        print('***', _10f30, file=_928cf)

    def _6057d(_928cf, _5487d, _4ab90, _1cabb, _e239c):
        if _4ab90()((':', ',')):
            return []
        try:
            _22ad2 = _928cf(_5487d, _4ab90, _1cabb, _e239c)
        except Exception:
            _22ad2 = []
        _3b569 = _62b74(_62b74(_5487d) + '*')
        for _256f7 in _3b569:
            if _3ba43(_256f7):
                _22ad2(_256f7 + '/')
            elif _3ba43(_256f7) and _256f7()(('.py', '.pyw')):
                _22ad2(_256f7 + ':')
        return _22ad2

    def _07cb3(_928cf, _5487d, _4ab90, _1cabb, _e239c):
        return [str(_8830d) for (_8830d, _bdd6e) in enumerate(_94215) if _bdd6e is not None and str(_8830d)(_5487d)]

    def _13bed(_928cf, _5487d, _4ab90, _1cabb, _e239c):
        if not _928cf:
            return []
        _b5fe6 = {**_928cf, **_928cf}
        if '.' in _5487d:
            _b66e7 = _5487d('.')
            try:
                _7e390 = _b5fe6[_b66e7[0]]
                for _c894a in _b66e7[1:-1]:
                    _7e390 = getattr(_7e390, _c894a)
            except (KeyError, AttributeError):
                return []
            _574f2 = '.'(_b66e7[:-1]) + '.'
            return [_574f2 + _2deaf for _2deaf in dir(_7e390) if _2deaf(_b66e7[-1])]
        else:
            return [_2deaf for _2deaf in _b5fe6() if _2deaf(_5487d)]

    def _477d6(_928cf, _95501):
        """commands [bpnumber]
        (com) ...
        (com) end
        (Pdb)

        Specify a list of commands for breakpoint number bpnumber.
        The commands themselves are entered on the following lines.
        Type a line containing just 'end' to terminate the commands.
        The commands are executed when the breakpoint is hit.

        To remove all commands from a breakpoint, type commands and
        follow it immediately with end; that is, give no commands.

        With no bpnumber argument, commands refers to the last
        breakpoint set.

        You can use breakpoint commands to start your program up
        again.  Simply use the continue command, or step, or any other
        command that resumes execution.

        Specifying any command resuming execution (currently continue,
        step, next, return, jump, quit and their abbreviations)
        terminates the command list (as if that command was
        immediately followed by end).  This is because any time you
        resume execution (even with a simple next or step), you may
        encounter another breakpoint -- which could have its own
        command list, leading to ambiguities about which list to
        execute.

        If you use the 'silent' command in the command list, the usual
        message about stopping at a breakpoint is not printed.  This
        may be desirable for breakpoints that are to print a specific
        message and then continue.  If none of the other commands
        print anything, you will see no sign that the breakpoint was
        reached.
        """
        if not _95501:
            _08730 = len(_94215) - 1
        else:
            try:
                _08730 = int(_95501)
            except:
                _928cf('Usage: commands [bnum]\n        ...\n        end')
                return
        try:
            _928cf(_08730)
        except ValueError as err:
            _928cf('cannot set commands: %s' % _9447b)
            return
        _928cf = _08730
        if _08730 in _928cf:
            _d92c1 = (_928cf[_08730], _928cf[_08730], _928cf[_08730])
        else:
            _d92c1 = None
        _928cf[_08730] = []
        _928cf[_08730] = True
        _928cf[_08730] = False
        _1f171 = _928cf
        _928cf = '(com) '
        _928cf = True
        try:
            _928cf()
        except KeyboardInterrupt:
            if _d92c1:
                _928cf[_08730] = _d92c1[0]
                _928cf[_08730] = _d92c1[1]
                _928cf[_08730] = _d92c1[2]
            else:
                del _928cf[_08730]
                del _928cf[_08730]
                del _928cf[_08730]
            _928cf('command definition aborted, old commands restored')
        finally:
            _928cf = False
            _928cf = _1f171
    _1874e = _07cb3

    def _dc60e(_928cf, _95501, _02bdb=0):
        """b(reak) [ ([filename:]lineno | function) [, condition] ]
        Without argument, list all breaks.

        With a line number argument, set a break at this line in the
        current file.  With a function name, set a break at the first
        executable line of that function.  If a second argument is
        present, it is a string specifying an expression which must
        evaluate to true before the breakpoint is honored.

        The line number may be prefixed with a filename and a colon,
        to specify a breakpoint in another file (probably one that
        hasn't been loaded yet).  The file is searched for on
        sys.path; the .py suffix may be omitted.
        """
        if not _95501:
            if _928cf:
                _928cf('Num Type         Disp Enb   Where')
                for _bdd6e in _94215:
                    if _bdd6e:
                        _928cf(_bdd6e())
            return
        _a30b9 = None
        _f91cc = None
        _91fde = None
        _b85a1 = _95501(',')
        if _b85a1 > 0:
            _91fde = _95501[_b85a1 + 1:]()
            _95501 = _95501[:_b85a1]()
        _2f009 = _95501(':')
        _29d12 = None
        if _2f009 >= 0:
            _a30b9 = _95501[:_2f009]()
            _d796e = _928cf(_a30b9)
            if not _d796e:
                _928cf('%r not found from sys.path' % _a30b9)
                return
            else:
                _a30b9 = _d796e
            _95501 = _95501[_2f009 + 1:]()
            try:
                _f91cc = int(_95501)
            except ValueError:
                _928cf('Bad lineno: %s' % _95501)
                return
        else:
            try:
                _f91cc = int(_95501)
            except ValueError:
                try:
                    _b96aa = eval(_95501, _928cf, _928cf)
                except:
                    _b96aa = _95501
                try:
                    if hasattr(_b96aa, '__func__'):
                        _b96aa = _b96aa
                    _bddd9 = _b96aa
                    _29d12 = _bddd9
                    _f91cc = _bddd9
                    _a30b9 = _bddd9
                except:
                    (_1c19c, _a30b9, _96b8c) = _928cf(_95501)
                    if not _1c19c:
                        _928cf('The specified object %r is not a function or was not found along sys.path.' % _95501)
                        return
                    _29d12 = _1c19c
                    _f91cc = int(_96b8c)
        if not _a30b9:
            _a30b9 = _928cf()
        _4ab90 = _928cf(_a30b9, _f91cc)
        if _4ab90:
            _9447b = _928cf(_a30b9, _4ab90, _02bdb, _91fde, _29d12)
            if _9447b:
                _928cf(_9447b)
            else:
                _bdd6e = _928cf(_a30b9, _4ab90)[-1]
                _928cf('Breakpoint %d at %s:%d' % (_bdd6e, _bdd6e, _bdd6e))

    def _40d73(_928cf):
        """Produce a reasonable default."""
        _a30b9 = _928cf
        if _a30b9 == '<string>' and _928cf:
            _a30b9 = _928cf
        return _a30b9
    _33b53 = _dc60e
    _c39cd = _6057d
    _b8e78 = _6057d

    def _d61d3(_928cf, _95501):
        """tbreak [ ([filename:]lineno | function) [, condition] ]
        Same arguments as break, but sets a temporary breakpoint: it
        is automatically deleted when first hit.
        """
        _928cf(_95501, 1)
    _bcce5 = _6057d

    def _14d0d(_928cf, _e9fa2):
        _ee2f6 = (None, None, None)
        _2a085 = _e9fa2("'")
        if len(_2a085) == 1:
            id = _2a085[0]()
        elif len(_2a085) == 3:
            id = _2a085[1]()
        else:
            return _ee2f6
        if id == '':
            return _ee2f6
        _b1f63 = id('.')
        if _b1f63[0] == 'self':
            del _b1f63[0]
            if len(_b1f63) == 0:
                return _ee2f6
        _c0a6f = _928cf()
        if len(_b1f63) == 1:
            _fae96 = _b1f63[0]
        else:
            _d796e = _928cf(_b1f63[0])
            if _d796e:
                _c0a6f = _d796e
            _fae96 = _b1f63[1]
        _523b8 = _cfbec(_fae96, _c0a6f)
        return _523b8 or _ee2f6

    def _23393(_928cf, _a30b9, _f91cc):
        """Check whether specified line seems to be executable.

        Return `lineno` if it is, 0 if not (e.g. a docstring, comment, blank
        line or EOF). Warning: testing is not comprehensive.
        """
        _b7a43 = getattr(_928cf, 'curframe', None)
        _3b569 = _b7a43 if _b7a43 else None
        _4ab90 = _7c5e6(_a30b9, _f91cc, _3b569)
        if not _4ab90:
            _928cf('End of file')
            return 0
        _4ab90 = _4ab90()
        if not _4ab90 or _4ab90[0] == '#' or _4ab90[:3] == '"""' or (_4ab90[:3] == "'''"):
            _928cf('Blank or comment')
            return 0
        return _f91cc

    def _d165c(_928cf, _95501):
        """enable bpnumber [bpnumber ...]
        Enables the breakpoints given as a space separated list of
        breakpoint numbers.
        """
        _0ad6b = _95501()
        for _8830d in _0ad6b:
            try:
                _bdd6e = _928cf(_8830d)
            except ValueError as err:
                _928cf(_9447b)
            else:
                _bdd6e()
                _928cf('Enabled %s' % _bdd6e)
    _fb0c2 = _07cb3

    def _f3463(_928cf, _95501):
        """disable bpnumber [bpnumber ...]
        Disables the breakpoints given as a space separated list of
        breakpoint numbers.  Disabling a breakpoint means it cannot
        cause the program to stop execution, but unlike clearing a
        breakpoint, it remains in the list of breakpoints and can be
        (re-)enabled.
        """
        _0ad6b = _95501()
        for _8830d in _0ad6b:
            try:
                _bdd6e = _928cf(_8830d)
            except ValueError as err:
                _928cf(_9447b)
            else:
                _bdd6e()
                _928cf('Disabled %s' % _bdd6e)
    _013d3 = _07cb3

    def _ac105(_928cf, _95501):
        """condition bpnumber [condition]
        Set a new condition for the breakpoint, an expression which
        must evaluate to true before the breakpoint is honored.  If
        condition is absent, any existing condition is removed; i.e.,
        the breakpoint is made unconditional.
        """
        _0ad6b = _95501(' ', 1)
        try:
            _91fde = _0ad6b[1]
        except IndexError:
            _91fde = None
        try:
            _bdd6e = _928cf(_0ad6b[0]())
        except IndexError:
            _928cf('Breakpoint number expected')
        except ValueError as err:
            _928cf(_9447b)
        else:
            _bdd6e = _91fde
            if not _91fde:
                _928cf('Breakpoint %d is now unconditional.' % _bdd6e)
            else:
                _928cf('New condition set for breakpoint %d.' % _bdd6e)
    _e4ac2 = _07cb3

    def _53844(_928cf, _95501):
        """ignore bpnumber [count]
        Set the ignore count for the given breakpoint number.  If
        count is omitted, the ignore count is set to 0.  A breakpoint
        becomes active when the ignore count is zero.  When non-zero,
        the count is decremented each time the breakpoint is reached
        and the breakpoint is not disabled and any associated
        condition evaluates to true.
        """
        _0ad6b = _95501()
        try:
            _a94c7 = int(_0ad6b[1]())
        except:
            _a94c7 = 0
        try:
            _bdd6e = _928cf(_0ad6b[0]())
        except IndexError:
            _928cf('Breakpoint number expected')
        except ValueError as err:
            _928cf(_9447b)
        else:
            _bdd6e = _a94c7
            if _a94c7 > 0:
                if _a94c7 > 1:
                    _b2fe8 = '%d crossings' % _a94c7
                else:
                    _b2fe8 = '1 crossing'
                _928cf('Will ignore next %s of breakpoint %d.' % (_b2fe8, _bdd6e))
            else:
                _928cf('Will stop next time breakpoint %d is reached.' % _bdd6e)
    _c3f50 = _07cb3

    def _14099(_928cf, _95501):
        """cl(ear) filename:lineno
cl(ear) [bpnumber [bpnumber...]]
        With a space separated list of breakpoint numbers, clear
        those breakpoints.  Without argument, clear all breaks (but
        first ask confirmation).  With a filename:lineno argument,
        clear all breaks at that line in that file.
        """
        if not _95501:
            try:
                _da848 = input('Clear all breaks? ')
            except EOFError:
                _da848 = 'no'
            _da848 = _da848()()
            if _da848 in ('y', 'yes'):
                _a68c5 = [_bdd6e for _bdd6e in _94215 if _bdd6e]
                _928cf()
                for _bdd6e in _a68c5:
                    _928cf('Deleted %s' % _bdd6e)
            return
        if ':' in _95501:
            _8830d = _95501(':')
            _a30b9 = _95501[:_8830d]
            _95501 = _95501[_8830d + 1:]
            try:
                _f91cc = int(_95501)
            except ValueError:
                _9447b = 'Invalid line number (%s)' % _95501
            else:
                _a68c5 = _928cf(_a30b9, _f91cc)[:]
                _9447b = _928cf(_a30b9, _f91cc)
            if _9447b:
                _928cf(_9447b)
            else:
                for _bdd6e in _a68c5:
                    _928cf('Deleted %s' % _bdd6e)
            return
        _7728f = _95501()
        for _8830d in _7728f:
            try:
                _bdd6e = _928cf(_8830d)
            except ValueError as err:
                _928cf(_9447b)
            else:
                _928cf(_8830d)
                _928cf('Deleted %s' % _bdd6e)
    _d89bd = _14099
    _d5b0d = _6057d
    _6b21b = _6057d

    def _d60c8(_928cf, _95501):
        """w(here)
        Print a stack trace, with the most recent frame at the bottom.
        An arrow indicates the "current frame", which determines the
        context of most commands.  'bt' is an alias for this command.
        """
        _928cf()
    _2f303 = _d60c8
    _0c93f = _d60c8

    def _e781b(_928cf, _cb7fa):
        assert 0 <= _cb7fa < len(_928cf)
        _928cf = _cb7fa
        _928cf = _928cf[_928cf][0]
        _928cf = _928cf
        _928cf(_928cf[_928cf])
        _928cf = None

    def _9eff7(_928cf, _95501):
        """u(p) [count]
        Move the current frame count (default one) levels up in the
        stack trace (to an older frame).
        """
        if _928cf == 0:
            _928cf('Oldest frame')
            return
        try:
            _a94c7 = int(_95501 or 1)
        except ValueError:
            _928cf('Invalid frame count (%s)' % _95501)
            return
        if _a94c7 < 0:
            _24ded = 0
        else:
            _24ded = max(0, _928cf - _a94c7)
        _928cf(_24ded)
    _be16a = _9eff7

    def _95eea(_928cf, _95501):
        """d(own) [count]
        Move the current frame count (default one) levels down in the
        stack trace (to a newer frame).
        """
        if _928cf + 1 == len(_928cf):
            _928cf('Newest frame')
            return
        try:
            _a94c7 = int(_95501 or 1)
        except ValueError:
            _928cf('Invalid frame count (%s)' % _95501)
            return
        if _a94c7 < 0:
            _24ded = len(_928cf) - 1
        else:
            _24ded = min(len(_928cf) - 1, _928cf + _a94c7)
        _928cf(_24ded)
    _96b1d = _95eea

    def _72d76(_928cf, _95501):
        """unt(il) [lineno]
        Without argument, continue execution until the line with a
        number greater than the current one is reached.  With a line
        number, continue execution until a line with a number greater
        or equal to that is reached.  In both cases, also stop when
        the current frame returns.
        """
        if _95501:
            try:
                _f91cc = int(_95501)
            except ValueError:
                _928cf('Error in argument: %r' % _95501)
                return
            if _f91cc <= _928cf:
                _928cf('"until" line number is smaller than current line number')
                return
        else:
            _f91cc = None
        _928cf(_928cf, _f91cc)
        return 1
    _535f3 = _72d76

    def _eb713(_928cf, _95501):
        """s(tep)
        Execute the current line, stop at the first possible occasion
        (either in a function that is called or in the current
        function).
        """
        _928cf()
        return 1
    _b99d7 = _eb713

    def _29fac(_928cf, _95501):
        """n(ext)
        Continue execution until the next line in the current function
        is reached or it returns.
        """
        _928cf(_928cf)
        return 1
    _5db54 = _29fac

    def _6b151(_928cf, _95501):
        """run [args...]
        Restart the debugged python program. If a string is supplied
        it is split with "shlex", and the result is used as the new
        sys.argv.  History, breakpoints, actions and debugger options
        are preserved.  "restart" is an alias for "run".
        """
        if _95501:
            import shlex as _bf818
            _30623 = _0c902[0:1]
            try:
                _0c902 = _bf818(_95501)
            except ValueError as e:
                _928cf('Cannot run %s: %s' % (_95501, _af6b1))
                return
            _0c902[:0] = _30623
        raise _883d8
    _5b1af = _6b151

    def _0fe48(_928cf, _95501):
        """r(eturn)
        Continue execution until the current function returns.
        """
        _928cf(_928cf)
        return 1
    _62457 = _0fe48

    def _484a9(_928cf, _95501):
        """c(ont(inue))
        Continue execution, only stop when a breakpoint is encountered.
        """
        if not _928cf:
            try:
                _43e42 = _3610b(_3610b, _928cf)
            except ValueError:
                pass
        _928cf()
        return 1
    _a3632 = _1775b = _484a9

    def _b6bd6(_928cf, _95501):
        """j(ump) lineno
        Set the next line that will be executed.  Only available in
        the bottom-most frame.  This lets you jump back and execute
        code again, or jump forward to skip code that you don't want
        to run.

        It should be noted that not all jumps are allowed -- for
        instance it is not possible to jump into the middle of a
        for loop or out of a finally clause.
        """
        if _928cf + 1 != len(_928cf):
            _928cf('You can only jump within the bottom frame')
            return
        try:
            _95501 = int(_95501)
        except ValueError:
            _928cf("The 'jump' command requires a line number")
        else:
            try:
                _928cf = _95501
                _928cf[_928cf] = (_928cf[_928cf][0], _95501)
                _928cf(_928cf[_928cf])
            except ValueError as e:
                _928cf('Jump failed: %s' % _af6b1)
    _867a8 = _b6bd6

    def _bef61(_928cf, _95501):
        """debug code
        Enter a recursive debugger that steps through the code
        argument (which is an arbitrary expression or statement to be
        executed in the current environment).
        """
        _0c902(None)
        globals = _928cf
        locals = _928cf
        _247e9 = _43e42(_928cf, _928cf, _928cf)
        _247e9 = '(%s) ' % _928cf()
        _928cf('ENTERING RECURSIVE DEBUGGER')
        try:
            _0c902(_247e9, (_95501, globals, locals))
        except Exception:
            _928cf()
        _928cf('LEAVING RECURSIVE DEBUGGER')
        _0c902(_928cf)
        _928cf = _247e9
    _72446 = _13bed

    def _7a0ae(_928cf, _95501):
        """q(uit)
exit
        Quit from the debugger. The program being executed is aborted.
        """
        _928cf = True
        _928cf()
        return 1
    _12f36 = _7a0ae
    _8ee1b = _7a0ae

    def _aaacc(_928cf, _95501):
        """EOF
        Handles the receipt of EOF as a command.
        """
        _928cf('')
        _928cf = True
        _928cf()
        return 1

    def _88165(_928cf, _95501):
        """a(rgs)
        Print the argument list of the current function.
        """
        _bd125 = _928cf
        dict = _928cf
        _2deaf = _bd125 + _bd125
        if _bd125 & _16436:
            _2deaf = _2deaf + 1
        if _bd125 & _16436:
            _2deaf = _2deaf + 1
        for _8830d in range(_2deaf):
            _647b9 = _bd125[_8830d]
            if _647b9 in dict:
                _928cf('%s = %r' % (_647b9, dict[_647b9]))
            else:
                _928cf('%s = *** undefined ***' % (_647b9,))
    _efce2 = _88165

    def _0e932(_928cf, _95501):
        """retval
        Print the return value for the last return of a function.
        """
        if '__return__' in _928cf:
            _928cf(repr(_928cf['__return__']))
        else:
            _928cf('Not yet returned!')
    _ce891 = _0e932

    def _fb90c(_928cf, _95501):
        try:
            return eval(_95501, _928cf, _928cf)
        except:
            _928cf()
            raise

    def _a68e6(_928cf, _95501, _b7a43=None):
        try:
            if _b7a43 is None:
                return eval(_95501, _928cf, _928cf)
            else:
                return eval(_95501, _b7a43, _b7a43)
        except:
            _ab41d = _0c902()[:2]
            _9447b = _df75f(*_ab41d)[-1]()
            return _077b6('** raised %s **' % _9447b)

    def _b7895(_928cf):
        _ab41d = _0c902()[:2]
        _928cf(_df75f(*_ab41d)[-1]())

    def _7c5f8(_928cf, _95501, _b96aa):
        try:
            _60a39 = _928cf(_95501)
        except:
            return
        try:
            _928cf(_b96aa(_60a39))
        except:
            _928cf()

    def _c62b7(_928cf, _95501):
        """p expression
        Print the value of the expression.
        """
        _928cf(_95501, repr)

    def _22526(_928cf, _95501):
        """pp expression
        Pretty-print the value of the expression.
        """
        _928cf(_95501, _d959d)
    _cfdac = _13bed
    _978c5 = _13bed
    _9e6b4 = _13bed

    def _ae315(_928cf, _95501):
        """l(ist) [first [,last] | .]

        List source code for the current file.  Without arguments,
        list 11 lines around the current line or continue the previous
        listing.  With . as argument, list 11 lines around the current
        line.  With one argument, list 11 lines starting at that line.
        With two arguments, list the given range; if the second
        argument is less than the first, it is a count.

        The current line in the current frame is indicated by "->".
        If an exception is being debugged, the line where the
        exception was originally raised or propagated is indicated by
        ">>", if it differs from the current line.
        """
        _928cf = 'list'
        _fef2f = None
        if _95501 and _95501 != '.':
            try:
                if ',' in _95501:
                    (_1c591, _fef2f) = _95501(',')
                    _1c591 = int(_1c591())
                    _fef2f = int(_fef2f())
                    if _fef2f < _1c591:
                        _fef2f = _1c591 + _fef2f
                else:
                    _1c591 = int(_95501())
                    _1c591 = max(1, _1c591 - 5)
            except ValueError:
                _928cf('Error in argument: %r' % _95501)
                return
        elif _928cf is None or _95501 == '.':
            _1c591 = max(1, _928cf - 5)
        else:
            _1c591 = _928cf + 1
        if _fef2f is None:
            _fef2f = _1c591 + 10
        _a30b9 = _928cf
        if _a30b9('<frozen'):
            _67c2e = _928cf('__file__')
            if isinstance(_67c2e, str):
                _a30b9 = _67c2e
        _8b5c1 = _928cf(_a30b9)
        try:
            _1b6c0 = _7c5e6(_a30b9, _928cf)
            _928cf(_1b6c0[_1c591 - 1:_fef2f], _1c591, _8b5c1, _928cf)
            _928cf = min(_fef2f, len(_1b6c0))
            if len(_1b6c0) < _fef2f:
                _928cf('[EOF]')
        except KeyboardInterrupt:
            pass
    _0a6d6 = _ae315

    def _afc0e(_928cf, _95501):
        """longlist | ll
        List the whole source code for the current function or frame.
        """
        _a30b9 = _928cf
        _8b5c1 = _928cf(_a30b9)
        try:
            (_1b6c0, _f91cc) = _16436(_928cf)
        except OSError as err:
            _928cf(_9447b)
            return
        _928cf(_1b6c0, _f91cc, _8b5c1, _928cf)
    _43d9c = _afc0e

    def _ff9ca(_928cf, _95501):
        """source expression
        Try to get source code for the given object and display it.
        """
        try:
            _7e390 = _928cf(_95501)
        except:
            return
        try:
            (_1b6c0, _f91cc) = _16436(_7e390)
        except (OSError, TypeError) as err:
            _928cf(_9447b)
            return
        _928cf(_1b6c0, _f91cc)
    _c4bd1 = _13bed

    def _b5e51(_928cf, _1b6c0, _bc462, _5bde0=(), _b7a43=None):
        """Print a range of lines."""
        if _b7a43:
            _36f02 = _b7a43
            _c630b = _928cf(_b7a43, -1)
        else:
            _36f02 = _c630b = -1
        for (_f91cc, _4ab90) in enumerate(_1b6c0, _bc462):
            _94bc3 = str(_f91cc)(3)
            if len(_94bc3) < 4:
                _94bc3 += ' '
            if _f91cc in _5bde0:
                _94bc3 += 'B'
            else:
                _94bc3 += ' '
            if _f91cc == _36f02:
                _94bc3 += '->'
            elif _f91cc == _c630b:
                _94bc3 += '>>'
            _928cf(_94bc3 + '\t' + _4ab90())

    def _bfe54(_928cf, _95501):
        """whatis arg
        Print the type of the argument.
        """
        try:
            _07ed6 = _928cf(_95501)
        except:
            return
        _bddd9 = None
        try:
            _bddd9 = _07ed6
        except Exception:
            pass
        if _bddd9:
            _928cf('Method %s' % _bddd9)
            return
        try:
            _bddd9 = _07ed6
        except Exception:
            pass
        if _bddd9:
            _928cf('Function %s' % _bddd9)
            return
        if _07ed6 is type:
            _928cf('Class %s.%s' % (_07ed6, _07ed6))
            return
        _928cf(type(_07ed6))
    _1ec75 = _13bed

    def _1e89a(_928cf, _95501):
        """display [expression]

        Display the value of the expression if it changed, each time execution
        stops in the current frame.

        Without expression, list all display expressions for the current frame.
        """
        if not _95501:
            _928cf('Currently displaying:')
            for _fae96 in _928cf(_928cf, {})():
                _928cf('%s: %r' % _fae96)
        else:
            _60a39 = _928cf(_95501)
            _928cf(_928cf, {})[_95501] = _60a39
            _928cf('display %s: %r' % (_95501, _60a39))
    _f714d = _13bed

    def _ee56b(_928cf, _95501):
        """undisplay [expression]

        Do not display the expression any more in the current frame.

        Without expression, clear all display expressions for the current frame.
        """
        if _95501:
            try:
                del _928cf(_928cf, {})[_95501]
            except KeyError:
                _928cf('not displaying %s' % _95501)
        else:
            _928cf(_928cf, None)

    def _f9a31(_928cf, _5487d, _4ab90, _1cabb, _e239c):
        return [_af6b1 for _af6b1 in _928cf(_928cf, {}) if _af6b1(_5487d)]

    def _73b20(_928cf, _95501):
        """interact

        Start an interactive interpreter whose global namespace
        contains all the (global and local) names found in the current scope.
        """
        _b5fe6 = {**_928cf, **_928cf}
        _bddd9('*interactive*', local=_b5fe6)

    def _7fa27(_928cf, _95501):
        """alias [name [command [parameter parameter ...] ]]
        Create an alias called 'name' that executes 'command'.  The
        command must *not* be enclosed in quotes.  Replaceable
        parameters can be indicated by %1, %2, and so on, while %* is
        replaced by all the parameters.  If no command is given, the
        current alias for name is shown. If no name is given, all
        aliases are listed.

        Aliases may be nested and can contain anything that can be
        legally typed at the pdb prompt.  Note!  You *can* override
        internal pdb commands with aliases!  Those internal commands
        are then hidden until the alias is removed.  Aliasing is
        recursively applied to the first word of the command line; all
        other words in the line are left alone.

        As an example, here are two useful aliases (especially when
        placed in the .pdbrc file):

        # Print instance variables (usage "pi classInst")
        alias pi for k in %1.__dict__.keys(): print("%1.",k,"=",%1.__dict__[k])
        # Print instance variables in self
        alias ps pi self
        """
        _0ad6b = _95501()
        if len(_0ad6b) == 0:
            _452ba = sorted(_928cf())
            for _a524c in _452ba:
                _928cf('%s = %s' % (_a524c, _928cf[_a524c]))
            return
        if _0ad6b[0] in _928cf and len(_0ad6b) == 1:
            _928cf('%s = %s' % (_0ad6b[0], _928cf[_0ad6b[0]]))
        else:
            _928cf[_0ad6b[0]] = ' '(_0ad6b[1:])

    def _b3511(_928cf, _95501):
        """unalias name
        Delete the specified alias.
        """
        _0ad6b = _95501()
        if len(_0ad6b) == 0:
            return
        if _0ad6b[0] in _928cf:
            del _928cf[_0ad6b[0]]

    def _38a50(_928cf, _5487d, _4ab90, _1cabb, _e239c):
        return [_67ebd for _67ebd in _928cf if _67ebd(_5487d)]
    _bb4c7 = ['do_continue', 'do_step', 'do_next', 'do_return', 'do_quit', 'do_jump']

    def _ca341(_928cf):
        try:
            for _8f483 in _928cf:
                _928cf(_8f483)
        except KeyboardInterrupt:
            pass

    def _c7d55(_928cf, _8f483, _5efb8=_7bf3a):
        (_b7a43, _f91cc) = _8f483
        if _b7a43 is _928cf:
            _574f2 = '> '
        else:
            _574f2 = '  '
        _928cf(_574f2 + _928cf(_8f483, _5efb8))

    def _74b81(_928cf, _95501):
        """h(elp)
        Without argument, print the list of available commands.
        With a command name as argument, print help about that command.
        "help pdb" shows the full pdb documentation.
        "help exec" gives help on the ! command.
        """
        if not _95501:
            return _feba2(_928cf, _95501)
        try:
            try:
                _18843 = getattr(_928cf, 'help_' + _95501)
                return _18843()
            except AttributeError:
                _e8224 = getattr(_928cf, 'do_' + _95501)
        except AttributeError:
            _928cf('No help for %r' % _95501)
        else:
            if _0c902 >= 2:
                _928cf('No help for %r; please do not run Python with -OO if you need command help' % _95501)
                return
            if _e8224 is None:
                _928cf('No help for %r; __doc__ string missing' % _95501)
                return
            _928cf(_e8224())
    _998d1 = _74b81

    def _7daf3(_928cf):
        """(!) statement
        Execute the (one-line) statement in the context of the current
        stack frame.  The exclamation point can be omitted unless the
        first word of the statement resembles a debugger command.  To
        assign to a global variable you must always prefix the command
        with a 'global' command, e.g.:
        (Pdb) global list_options; list_options = ['-l']
        (Pdb)
        """
        _928cf((_928cf or '')())

    def _1dcbc(_928cf):
        help()

    def _1578a(_928cf, _a30b9):
        """Helper function for break/clear parsing -- may be overridden.

        lookupmodule() translates (possibly incomplete) file or module name
        into an absolute file name.
        """
        if _3ba43(_a30b9) and _3ba43(_a30b9):
            return _a30b9
        _d796e = _3ba43(_0c902[0], _a30b9)
        if _3ba43(_d796e) and _928cf(_d796e) == _928cf:
            return _d796e
        (_7f81c, _ddc33) = _3ba43(_a30b9)
        if _ddc33 == '':
            _a30b9 = _a30b9 + '.py'
        if _3ba43(_a30b9):
            return _a30b9
        for _4bac3 in _0c902:
            while _3ba43(_4bac3):
                _4bac3 = _3ba43(_4bac3)
            _c9949 = _3ba43(_4bac3, _a30b9)
            if _3ba43(_c9949):
                return _c9949
        return None

    def _15ef3(_928cf, _f6e83: Union[_ModuleTarget, _ScriptTarget]):
        _928cf = True
        _928cf = False
        _928cf = _928cf(_f6e83)
        import __main__ as _a7d35
        __main__()
        __main__(_f6e83)
        _928cf(_f6e83)
if __doc__ is not None:
    _a70b7 = ['help', 'where', 'down', 'up', 'break', 'tbreak', 'clear', 'disable', 'enable', 'ignore', 'condition', 'commands', 'step', 'next', 'until', 'jump', 'return', 'retval', 'run', 'continue', 'list', 'longlist', 'args', 'p', 'pp', 'whatis', 'source', 'display', 'undisplay', 'interact', 'alias', 'unalias', 'debug', 'quit']
    for _5dff4 in _a70b7:
        __doc__ += getattr(_43e42, 'do_' + _5dff4)() + '\n\n'
    __doc__ += _43e42
    del _a70b7, _5dff4

def _b3131(_3d3ad, _17b58=None, _706c6=None):
    """Execute the *statement* (given as a string or a code object)
    under debugger control.

    The debugger prompt appears before any code is executed; you can set
    breakpoints and type continue, or you can step through the statement
    using step or next.

    The optional *globals* and *locals* arguments specify the
    environment in which the code is executed; by default the
    dictionary of the module __main__ is used (see the explanation of
    the built-in exec() or eval() functions.).
    """
    _43e42()(_3d3ad, globals, locals)

def _e9645(_bad54, _17b58=None, _706c6=None):
    """Evaluate the *expression* (given as a string or a code object)
    under debugger control.

    When runeval() returns, it returns the value of the expression.
    Otherwise this function is similar to run().
    """
    return _43e42()(_bad54, globals, locals)

def _1aee0(_3d3ad, _17b58, _706c6):
    _b3131(_3d3ad, globals, locals)

def _97dd7(*args, **kwds):
    """Call the function (a function or method object, not a string)
    with the given arguments.

    When runcall() returns, it returns whatever the function call
    returned. The debugger prompt appears as soon as the function is
    entered.
    """
    return _43e42()(*_0ad6b, **_831b9)

def _475b4(*, _64284=None):
    """Enter the debugger at the calling stack frame.

    This is useful to hard-code a breakpoint at a given point in a
    program, even if the code is not otherwise being debugged (e.g. when
    an assertion fails). If given, *header* is printed to the console
    just before debugging begins.
    """
    _3da86 = _43e42()
    if _64284 is not None:
        _3da86(_64284)
    _3da86(_0c902())

def _21866(_b5f61=None):
    """Enter post-mortem debugging of the given *traceback* object.

    If no traceback is given, it uses the one of the exception that is
    currently being handled (an exception must be being handled if the
    default is to be used).
    """
    if _b5f61 is None:
        _b5f61 = _0c902()[2]
    if _b5f61 is None:
        raise ValueError('A valid traceback must be passed if no exception is being handled')
    _247e9 = _43e42()
    _247e9()
    _247e9(None, _b5f61)

def _dddf1():
    """Enter post-mortem debugging of the traceback found in sys.last_traceback."""
    if hasattr(_0c902, 'last_exc'):
        _ba267 = _0c902
    else:
        _ba267 = _0c902
    _21866(_ba267)
_3ae26 = 'import x; x.main()'

def _cf94d():
    _b3131(_3ae26)

def _b43a1():
    import pydoc as _cc922
    _cc922(__doc__)
_715c0 = 'usage: pdb.py [-c command] ... [-m module | pyfile] [arg] ...\n\nDebug the Python program given by pyfile. Alternatively,\nan executable module or package to debug can be specified using\nthe -m switch.\n\nInitial commands are read from .pdbrc files in your home directory\nand in the current directory, if they exist.  Commands supplied with\n-c are executed after commands from .pdbrc files.\n\nTo let the script run until an exception occurs, use "-c continue".\nTo let the script run up to a given line X in the debugged file, use\n"-c \'until X\'".'

def _17563():
    import getopt as _a5c14
    (_22410, _0ad6b) = _a5c14(_0c902[1:], 'mhc:', ['help', 'command='])
    if not _0ad6b:
        print(_715c0)
        _0c902(2)
    if any((_6effe in ['-h', '--help'] for (_6effe, _295f6) in _22410)):
        print(_715c0)
        _0c902()
    _7dfb6 = [_295f6 for (_6effe, _295f6) in _22410 if _6effe in ['-c', '--command']]
    _e1d51 = any((_6effe in ['-m'] for (_6effe, _295f6) in _22410))
    _5ead7 = _a0cea if _e1d51 else _8a7ac
    _f6e83 = _5ead7(_0ad6b[0])
    _f6e83()
    _0c902[:] = _0ad6b
    _3da86 = _43e42()
    _3da86(_7dfb6)
    while True:
        try:
            _3da86(_f6e83)
            if _3da86:
                break
            print('The program finished and will be restarted')
        except _883d8:
            print('Restarting', _f6e83, 'with arguments:')
            print('\t' + ' '(_0c902[1:]))
        except SystemExit:
            print('The program exited via sys.exit(). Exit status:', end=' ')
            print(_0c902()[1])
        except SyntaxError:
            _df75f()
            _0c902(1)
        except:
            _df75f()
            print('Uncaught exception. Entering post mortem debugging')
            print("Running 'cont' or 'step' will restart the program")
            _b5f61 = _0c902()[2]
            _3da86(None, _b5f61)
            print('Post mortem debugger finished. The ' + _f6e83 + ' will be restarted')
if __name__ == '__main__':
    import pdb as _3da86
    _3da86()
