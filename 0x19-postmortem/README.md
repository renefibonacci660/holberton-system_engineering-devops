Issue Summary:
The entire duration of this outage was about 8 hours from the first occurance to the resolution.In this particular instance the incidence caused the whole companies internet speeds to slow to a hault and the entire building's VOIP phones to have noise quality issues and intermittently drop calls altogether. On the caller's end trying to reach any of the department's they were only intermittently having their calls answered, heard a busy tone or could hear a garbled voice before the calls dropped. As the issue progressed 100% of the users were effected; both the employee's phones and internet and the customers attempting to reach the support department via SMS or call. This issue was caused by two compounding problems; firstly the company had not properly accounted for the increased influx of calls that would occur with the increased customer base from their recent expansion. Secondly, since these phones were on a VOIP system that was not on a dedicated internet connection but hardwired into the same fiber connection it caused the employees internet connections to slow then hault completely. Any attempts at getting a dynamic LAN address were denied by rebooted phones/computers since the system froze. 

Timeline (format bullet point, format: time - keep it short, 1 or 2 sentences) must contain:
The issue was detected by customers and employees having call/internet quality issues 45 minutes after opening at 8:45am on a Monday after a new group addition of customers.

actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)
misleading investigation/debugging paths that were taken
which team/individuals was the incident escalated to
how the incident was resolved

Root Cause and Resolution:

explain in detail what was causing the issue
explain in detail how the issue was fixed
Corrective and preventative measures must contain:

what are the things that can be improved/fixed (broadly speaking)
a list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory…)