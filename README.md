Borderlands 3 Hotfix-Based Modding
==================================

There is no traditional modding in BL3 (as of October 20, 2019) like there
is for BL2/TPS.  In the meantime, though, while that's being figured out,
there is *technically* a method which could be used by enterprising and
technically savvy would-be modders: intercepting the GBX-provided
hotfixes as they're sent from the servers, and injecting your own
modifications.

This page won't go into details on how exactly to accomplish the first
bit (namely, intercepting the hotfixes).  Given the nature of this
activity, anyone attempting to do so should at least have the ability
to learn how to do it on your own.  There are many utilities out there
which are geared to this kind of on-the-wire editing, such as
[Charles](https://www.charlesproxy.com/), or the one I use,
[mitmproxy](https://mitmproxy.org/).

Remember that there's two components to successfully deploying a
MITM against yourself:

1. Intercepting the network traffic itself
2. Making sure the MITM'd app trusts the SSL cert that you're using
   to do the interception

Pay particular attention to point number 2, and make sure you
understand the security ramifications of what you're doing.  Ideally
your trust alterations are being done in as targetted a manner as
possible.

So: before going any further in here, make sure you've at least got
that much already working.  BL3 should be asking for hotfixes, and
your stuff should be intercepting that traffic enroute, with the
capability to alter it before it makes it back to the game.

Some Hotfix Details
-------------------

The next step, then, is to actually start altering hotfixes, or
at least adding your own.  If you take a look at the data being
sent over from GBX to the game, it's just
[JSON](https://en.wikipedia.org/wiki/JSON), and there's basically
just one big array which would need to be added to, if you want
to add your own hotfixes.  Each hotfix has a unique `key`, which
also defines when exactly the hotfix will be run, and a `value`,
which is the hotfix itself.

If you already know how BL2/TPS hotfixes work on the backend,
the BL3 hotfixes will seem reasonably familiar.  Some documentation
on the BL2/TPS hotfixes can be found on the BLCMods wiki on a
few pages: [Tutorial: Hotfix Data](https://github.com/BLCM/BLCMods/wiki/Tutorial:-Hotfix-Data#internal-structure)
and [Anatomy of a Mod File](https://github.com/BLCM/BLCMods/wiki/Anatomy-of-a-Mod-File#hotfixes).

There's definitely some differences for the BL3 versions, though,
and I've been starting to document those on the BLCMods wiki as
well: [Borderlands 3 Hotfixes](https://github.com/BLCM/BLCMods/wiki/Borderlands-3-Hotfixes).
You'll want to take a look through there to get a feel for what
hotfixes look like, because if you're constructing them by hand
you'll need to know what they look like.

One of the best resources for knowing exactly how BL3 hotfixes
do their thing is by looking at the *existing* BL3 hotfixes.
There's an archive of BL3 hotfixes which has been collecting data
since a week or so after the release of Borderlands 3, which
can be found here: [BLCM's "bl3hotfixes"](https://github.com/BLCM/bl3hotfixes/).
Additionally, I've got a Google Sheets page which has the total
collected hotfixes which have been used by GBX (including ones
which are no longer active), divided out into columns which can
make analysis a lot easier.  That sheet [can be found here](https://drive.google.com/open?id=1kfkC2hJs0hZSr12bvrQlY0GyEH4S_KAI_xIAqnGmKnQ).

Modifying the Hotfixes with mitmproxy
-------------------------------------

mitmproxy provides a very handy programmatic API, in Python, which
you can use to process streams that you've intercepted, which is
what I ended up using to make injection pretty easy on myself.
Specifically, I'm using mitmproxy's `mitmdump` command, with a
`-s hfinject.py` argument so that it uses my hotfix injection code.

What `hfinject.py` does is it first looks for a file called
`injectdata/modlist.txt`, which can look like this:

    # 10-Year Anniversary Events
    2019-10-01_-_10-year-anniversary-event-1_-_bonus_boss_loot
    better_rare_spawn_hunt
    better_eridium_event

    # Maggie super buff
    maggie_super_buff

    # Cheaper SDUs
    cheaper_sdus

As you can see, lines can be commented using a hash (`#`) sign,
and blank lines are ignored.  Each other non-commented line
should be a name of a mod that you want to load, which will
live on the filesystem as `injectdata/modname.txt`.  So those
live alongside the `modlist.txt` itself.  You can make changes
to `modlist.txt` at any time and the injection script will
re-load it the next time it intercepts a hotfix request.

For the mod files themselves, I didn't care enough to do too
much abstraction, so they are very nearly just the raw hotfix
format.  For instance, `maggie_super_buff.txt` looks like this:

    ###
    ### Super buff to Maggie, so I can just power through those
    ### interminable Circles of Slaughter.
    ###
    ### Original damage scale: 0.35
    ### Damage scale after GBX nerf: 0.15
    ###

    prefix: Maggie

    SparkPatchEntry,(1,2,0,),/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/_Unique/DataTable_WeaponBalance_Unique_JAK.DataTable_WeaponBalance_Unique_JAK,PS_Maggie,DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53,0,,50.000000

As you can see, the hotfix line itself is practically identically
identical to the "raw" hotfix format, though it's prefixed by
an additional field, which is `SparkPatchEntry` for this one.
The line which reads `prefix: Maggie` is important as well, and is
there so that the hotfix keys get assigned uniquely.  The hotfix
key for that statement, for instance, will end up being
`SparkPatchEntry-ApocMaggie1`.  If there were more than one hotfix
in that mod file, the next would be `SparkPatchEntry-ApocMaggie2`,
or `SparkLevelPatchEntry-ApocMaggie2`, etc.

I agree that specifying a `prefix` in the file like that is
especially lazy, but that way I don't have to worry about doing
global unique identifiers, since mods can be toggled on/off at
any time by editing that `modlist.txt` file.  **NOTE:** Remember
that the prefixes should be unique for each mod file that you've
got loaded, so the onus is on you for that.

As with `modlist.txt`, if a mod file itself changes, `hfinject.py`
will automatically re-load it when the next hotfix verification
happens.

Note that you should **not** escape quote marks in the hotfixes
you put in the mod files -- if you look at the raw JSON data,
you'll see that quotes are escaped, since they're inside of
JSON strings, but `hfinject.py` will take care of doing that
escpaing for you.

Triggering Hotfix Reloads
-------------------------

The quickest way to have the game re-load hotfixes from the server
is to head out to the main menu, hit `Quit`, and then select
`Title Screen` rather than `Desktop`.  That'll cause the main
menu to revert back to showing the Borderlands logo, logging you
back in to Shift, and then panning down to the usual waiting screen.
Within a few seconds the game should have reloaded hotfixes.
(If using mitmproxy, it's easy to look at its output to know for
sure whether or not the hotfixes have been requested.)

Note that when re-loading hotfixes like that, the game tends to
disconnect from shift within a few seconds, after getting the
hotfix data.  If you look at your mitmdump console output, you'll
see a couple of log lines like:

    x.x.x.x:41818: serverdisconnect
    x.x.x.x:41818: clientdisconnect

If you **don't** see those lines after a few seconds, it
sometimes means that you've screwed up some hotfix syntax
somewhere, and the hotfixes which were sent over to the game
haven't been fully loaded in yet.  So I'll often wait to see
those disconnect notices before proceeding to testing the mods.

Note that that quick disconnect generally does *not* happen
on the very first hotfix load, though.  Or at least not nearly
as quickly.

Getting Data
------------

BL2/TPS provided us with a very nice `obj dump` command from the
console, which was used to generate the wonderful set of data that
[BLCMM](https://github.com/BLCM/BLCMods/wiki/Borderlands-Community-Mod-Manager)'s OE
and [FT/BLCMM Explorer](https://github.com/apocalyptech/ft-explorer)
use, but unfortunately that's not available in BL3, so getting
data is pretty spotty.

You can actually get a fair amount of information just by
unencrypting/uncompressing the Borderlands 3 data packs.  You'll have
to Google around to figure out how to do that; it'll involve using
an official Unreal Engine utility (make sure you've got the right
version), and knowing the encryption key used on the data.  Once you
have the unpacked data files (you can copy all the content from
`OakGame/Content` into the main directory to avoid having files split
between two locations, btw), the `*.uasset` files can be handy.
If you have a program that looks for plaintext strings inside
binary files (like the UNIX mainstay [strings](https://en.wikipedia.org/wiki/Strings_%28Unix%29)),
you can get a list of all attribute names in that object, all
other objects which it references, and so on.  There's definitely
a lot of guesswork involved, but you can find a surprising amount
just by looking at that.  One thing we *cannot* do at this level,
yet, is find out what the actual values are to any attributes.

If you want something a little more sophisticated, there is a DLL
Injection technique available which can enable the BL3 console.
Even without a functional `obj dump`, the command `getall` still
exists, so you should be able to run, for instance,
`getall ItemPoolData BalancedItems`, to get a list of what all
currently-loaded item pools can drop.  I haven't been able to test
that out myself, though, since I'm on Linux, and I haven't
managed to get any DLL Injection technique to work in Wine/Proton.

Finally, of course, looking through the existing hotfixes that GBX
have been using can be a real help, as mentioned above.

Mods
----

I've got all the stuff that I've been working on in the `injectdata`
folder in here, so feel free to take a look in there.  The README
in that directory should have some short descriptions of everything.

License
-------

All the code in this project is licensed under the
[GPLv3 or later](https://www.gnu.org/licenses/quick-guide-gplv3.html).
See [COPYING.txt](COPYING.txt) for the full text of the license.
