# Test prompts for temenos-skills

Paste these one at a time into a fresh Claude Code session (in this project directory)
to manually verify each skill triggers correctly and produces sensible output. Each
skill has one prompt aimed squarely at it, plus a routing prompt to check `temenos-dev`
sends work to the right sub-skill.

For every prompt, the pass bar is:
1. The correct skill actually triggers (check the transcript/skill-invocation banner).
2. It follows the CLAUDE.md field-verification gate where relevant (states verified
   fields against `table-schema/<APP>.md` before emitting code, or halts and asks if a
   field can't be found — never invents one).
3. Output looks structurally correct for the artefact type (headers, $PACKAGE, error
   handling, etc. per skill conventions).

---

## 1. temenos-dev (entry point / router)
> "I need to add a validation on ACCOUNT so that AC.CATEGORY can't be changed once the
> account is authorised for the first time. What T24 artefact type should this be, and
> which fields do I need to check first?"

Pass check: routes to Step 1 classification (VAR/VCRR), then Step 2 schema verification
against `table-schema/ACCOUNT.md` before suggesting any field names.

## 2. temenos-infobasic
> "Write a VVR routine for CUSTOMER that defaults CUSTOMER.STATUS1 to '1' if it's not
> supplied at input, and rejects the record with an error if MNEMONIC is longer than
> 35 characters."

Pass check: verifies `CUSTOMER.STATUS1` / `MNEMONIC` exist in `table-schema/CUSTOMER.md`,
generates a VVR with proper file header, $PACKAGE, STORE.END.ERROR/error handling.

## 3. temenos-l3
> "I need a RecordLifecycle hook in Java for the ACCOUNT application that calls
> validateRecord to block authorisation if the account's working balance would go
> negative. Show me the full class with the correct superclass and method signature."

Pass check: uses the real RecordLifecycle/validateRecord signature, correct package/
import structure, CSD-standard header.

## 4. temenos-jbc
> "Write a jBC WRITE API component method for a custom package MY.BANK that builds an
> OFS record for ACCOUNT and calls OfsBuildRecord, then handles the response with
> setE on failure."

Pass check: correct $PACKAGE/$USING, metamodelVersion, OfsBuildRecord/setE usage,
compilable jBC structure.

## 5. temenos-de
> "Set up an ApplicationHandoff routine for FT (Funds Transfer) in package MY.BANK
> that maps the debit and credit account numbers into Array.5 positions for our
> DE.EVENT.MAPPING template, and explain how the fields routine ties in."

Pass check: correct ApplicationHandoff structure for FT, Array.5 mapping conventions,
`<PKG>` placeholder usage explained.

## 6. temenos-admin
> "TAFJ won't start on JBoss EAP after we pointed tafj.properties at a new Oracle DB —
> startjboss.sh throws a 'tools.jar not found' error on JDK21. What's actually wrong
> and which config file should I check first?"

Pass check: references TAFJ_HOME layout (conf/dbdrivers/appserver), tafj.properties,
correctly frames this as a known JDK21/tools.jar install issue, not code generation.

## 7. temenos-migration
> "We're upgrading from TAFJ R23 to R25. I have a Patch.xml from Temenos support —
> how do I tell which directories it will touch before I run the installer, and how
> do RELEASE manifests fit into verifying the upgrade afterwards?"

Pass check: explains the Patch.xml contract and RELEASE manifest interpretation,
doesn't drift into writing customisation code.

## 8. temenos-integration
> "We need to wire up a new payment scheme through the ESB — where does the OFS
> message layer (ofsml) sit relative to bnk/ESBProjects and bnk/Extensions, and where
> would a custom EB_ service-extension module plug in for entitlement checks?"

Pass check: correctly describes ESB/NonESB project layout, service-extension module
naming (EB_*/IF_*/etc.), doesn't try to hand-write jBC/Infobasic itself.

## 9. temenos-devsecops
> "Our JBC precompiler is rejecting a routine during the Maven build but the error
> is vague. How do I turn on remote debugging against TAFJ so I can step through the
> precompiled class, and how does this interact with the unit test framework?"

Pass check: references JBC precompiler rules, remote debugger setup, TAFJ Maven
plugin — tooling/process framing, not runtime-admin or code-gen framing.

## 10. temenos-architect
> "How is the base T24_BP routine repository organised by naming prefix — what's the
> difference between a CONV.*, V.*, and OC.* routine, and where would a brand-new
> custom component for my package sit relative to bnk/Extensions?"

Pass check: explains T24_BP naming-prefix conventions and componentisation model
without drifting into ESB/integration topology (that's temenos-integration's job) or
runtime config (temenos-admin's job).

---

## Bonus: sub-skill boundary check
> "Explain the difference between what temenos-admin, temenos-migration,
> temenos-integration, temenos-devsecops, and temenos-architect each cover, and give
> me one example question that would route to each."

Pass check: if this triggers any of the five, it should self-report the boundaries
correctly (each skill's own SKILL.md states what it does *not* cover and where to
route instead) — good smoke test that the routing lines drawn between the five new
R25-grounded skills are coherent, not overlapping.
