Completed 2026-03-25

I messed around with `lyric-reader.py`, including creating a fake flag file
locally at `flag.txt` to try to get the script to trigger reading it. I also
pasted the song lyrics into its own file so I didn't have to subtract in my head
to figure out what 'lip' (line) we were on.

The flag is printed at the end of the "secret intro", so the challenge can be
solved by getting the program to jump to the beginning of the song text.

Eventually I realized the program logic will interpret `;` as a line separator
and execute whatever comes after it as a command, so I solved this challenge by
injecting `;RETURN 0`.
