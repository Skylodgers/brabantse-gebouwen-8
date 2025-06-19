import re
from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(re.sub(r"_", r"-", r"brabantse_gebouwen"), "brabantse_gebouwen.urls", name="brabantse_gebouwen"),
)
