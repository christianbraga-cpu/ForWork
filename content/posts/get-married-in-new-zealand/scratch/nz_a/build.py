import json
OUT='/home/user/ForWork/content/posts/get-married-in-new-zealand/03-source-pack.json'
G='https://www.govt.nz/browse/family-and-whanau/getting-married/'
H='https://www.govt.nz/browse/family-and-whanau/getting-married/how-to-get-married-in-nz/'
D='https://www.doc.govt.nz/get-involved/apply-for-permits/business-or-activity/'
def f(i,c,s,t='government'): return {"fact_id":f"fact_{i:02d}","claim":"As at November 2026, "+c,"source":s,"source_type":t,"checked":"2026-11-17","is_price":False}
facts=[
 f(1,"the New Zealand Government 'Getting married' page (govt.nz, read in full) states: before you get married, you need to apply for a marriage licence, which confirms it is legal for you to marry. A fee applies.",G),
 f(2,"govt.nz 'Getting married' states: only registered celebrants can perform weddings or civil unions in New Zealand.",G),
 f(3,"govt.nz 'Getting married' states: a New Zealand marriage certificate is an official record of the marriage; it can be ordered online and posted. A fee applies.",G),
 f(4,"govt.nz 'Getting married' states: if you get married overseas you usually do not need to do anything in New Zealand beforehand; check with that country's officials.",G),
 f(5,"govt.nz 'How to get married in NZ' (read in full) states: you must get married by a celebrant, and you choose between a personalised ceremony and a registry ceremony.",H),
 f(6,"govt.nz 'How to get married in NZ' states: most marriage ceremonies in New Zealand are personalised; you work with a celebrant to design the ceremony, you can hold it at any time, date and place you want, and you write your own vows. A fee applies for the licence, plus the celebrant's own charge.",H),
 f(7,"govt.nz 'How to get married in NZ' states: a registry ceremony has standard vows and must take place during business hours on a weekday (9am to 5pm, Monday to Friday), not on a public holiday.",H),
 f(8,"govt.nz 'How to get married in NZ' states: for a registry ceremony a set ceremony fee applies, paid to the celebrant in advance, on top of the licence fee, and you should contact your celebrant before applying for a marriage licence to make sure they will be available.",H),
 f(9,"govt.nz 'Getting married' states: anyone who thinks there are legal reasons why someone should not marry can lodge a caveat or notice of objection.",G),
 f(10,"the Department of Conservation (doc.govt.nz) page 'Running your business or activity on DOC land', per its search-result snippet only (page not read in full): if you want to use public conservation land to run a business or activity you must get permission from DOC in the form of a concession. The page does not, in the text seen, name weddings.",D),
]
V=[
 "[[VERIFY: Marriage licence application detail. The govt.nz 'Get a marriage licence' page was not read: online vs paper application, statutory declaration, ID documents, how far ahead to apply, any waiting period (a non-official snippet says 3 working days), licence validity period, and whether non-residents can apply.]]",
 "[[VERIFY: Whether overseas visitors need any minimum stay or residency to marry in New Zealand. No official page read states this.]]",
 "[[VERIFY: Witness requirement (two witnesses), signing on the day and how the celebrant returns the paperwork for registration. Not on the pages read.]]",
 "[[VERIFY: Certificate types (e.g. printout vs certificate), processing time after the ceremony, and Apostille process and timing from the DIA Authentication Unit. dia.govt.nz/Authentications did not return readable text.]]",
 "[[VERIFY: Whether a wedding ceremony on public conservation land needs a DOC concession or a one-off permit, and lead time. Only a DOC search snippet was seen; no wedding-specific DOC page read.]]",
]
env={"agent":"planner-sme","task_id":"get-married-in-new-zealand","stage":"03","status":"needs_input","round":1,
"inputs_used":[
 "mcp__Apify__apify--web-fetch, one parallel round, 17 November 2026, no retries: https://www.govt.nz/browse/family-and-whanau/getting-married/ (200, read in full); https://www.govt.nz/browse/family-and-whanau/getting-married/how-to-get-married-in-nz/ (200, read in full); https://www.dia.govt.nz/Authentications (415, unsupported content type, not read)",
 "mcp__Apify__apify--web-search, 17 November 2026, two queries: DOC wedding concession; govt.nz marriage licence overseas visitors. Used to locate pages; one DOC snippet recorded (fact_10). Non-official results not used as facts.",
 "content/posts/get-married-in-new-zealand/00-input.json",
 "content/posts/getting-married-in-costa-rica/03-source-pack.json (structure reference)"],
"self_qa":{"checks":[
 {"check":"Every fact has a source and date","pass":True},
 {"check":"No price without a source; all prices in needs_signoff","pass":True,"note":"No amounts recorded; pages state amounts, written as 'a fee applies'."},
 {"check":"Every must-include covered or [[VERIFY]]","pass":True,"note":"Most licence-process items are [[VERIFY]] because the core licence page was not read."},
 {"check":"No invented quotes, statistics or real weddings","pass":True}],"confidence":0.35},
"open_questions":[
 {"to":"orchestrator","question":"The core govt.nz 'Get a marriage licence' page was NOT read (fast mode, one read round). Read https://www.govt.nz/browse/family-and-whanau/getting-married/get-a-marriage-licence/ (and its apply-online subpage) for: non-resident eligibility, online/paper application, statutory declaration, ID, lead time and waiting period, licence validity, witnesses, after-ceremony registration and certificate timing.","blocking":True},
 {"to":"orchestrator","question":"DIA Authentication Unit page (https://www.dia.govt.nz/Authentications) returned 415 to a text fetch. Refetch with formats ['raw'] or default, or use the govt.nz apostille page, for Apostille process and timing.","blocking":False},
 {"to":"orchestrator","question":"No wedding-specific DOC page read. Read https://www.doc.govt.nz/get-involved/apply-for-permits/business-or-activity/ and search doc.govt.nz for 'wedding' / 'one-off event' before the article says anything about ceremonies on conservation land.","blocking":False},
 {"to":"luxury-writer","question":"State NZ rules 'as at November 2026' with the line that the Wedded Advisor confirms current requirements. Never state a fee amount. No same-sex legal facts. No venue names. Registry ceremony weekday-hours rule (fact_07) applies to registry ceremonies only, not personalised ones.","blocking":False}],
"assumptions":["Must-include list taken from the orchestrator's batch A task (NZ legal side only).","Facts dated 17 November 2026, the date of reading. All facts from New Zealand government pages; DOC fact_10 is snippet-only and labelled so.","Non-official search snippets (TRACE, Tripadvisor, expat.com, celebrant blogs) were not recorded as facts; the 3-working-day claim appears only inside a VERIFY item as a lead to check."],
"verify_items":V,"tools_used":["mcp__Apify__apify--web-search","mcp__Apify__apify--web-fetch","Bash"],"next_agent":["luxury-writer"]}
cov=[
 {"item":"Who can marry; overseas visitors / non-residents, no residency","covered_by":[V[0],V[1]]},
 {"item":"Applying for a marriage licence (online or paper), lead time, waiting period","covered_by":["fact_01","fact_08",V[0]]},
 {"item":"Statutory declaration and documents / ID","covered_by":[V[0]]},
 {"item":"Licence validity period","covered_by":[V[0]]},
 {"item":"Who performs it (registered celebrant or registry ceremony)","covered_by":["fact_02","fact_05","fact_06","fact_07","fact_08"]},
 {"item":"Two witnesses","covered_by":[V[2]]},
 {"item":"Where the ceremony can take place","covered_by":["fact_06","fact_07"]},
 {"item":"After the ceremony: signing, registration, certificate, timing; certificate types","covered_by":["fact_03",V[2],V[3]]},
 {"item":"Fees ('a fee applies')","covered_by":["fact_01","fact_03","fact_06","fact_08"]},
 {"item":"Apostille for an NZ certificate (DIA Authentication Unit)","covered_by":[V[3]]},
 {"item":"DOC concessions on conservation land","covered_by":["fact_10",V[4]]},
]
ins=[
 {"detail":"Choose the ceremony type before anything else. A registry ceremony is locked to weekday business hours and standard vows, so a Saturday celebration at a chosen location means a personalised ceremony with a registered celebrant.","fact_ids":["fact_05","fact_06","fact_07"]},
 {"detail":"Lock in the celebrant first, then apply for the licence. The government guidance tells couples to confirm the celebrant's availability before applying.","fact_ids":["fact_02","fact_08"]},
 {"detail":"Order the marriage certificate online after the wedding and allow for postage to Australia before planning any name changes or paperwork back home.","fact_ids":["fact_03"]},
]
def save(n):
  env["payload"]={"facts":facts[:n],"insider_details":ins if n>=len(facts) else [],"quotes":[],"real_weddings":[],"verify_items":V,"needs_signoff":[],"must_include_coverage":cov}
  json.dump(env,open(OUT,'w'),indent=2,ensure_ascii=False)
for n in range(3,len(facts)+3,3): save(min(n,len(facts)))
