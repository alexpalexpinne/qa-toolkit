# Safe values

Values that cannot belong to a real person, account, or system. Prefer the
team's own test values (from `team-conventions.md`) over these, and prefer
values a provider or authority documents for testing over anything you
generate.

If you are not sure a value is reserved or documented for testing, do not
present it as safe: say what it is based on, or ask the user.

## Reserved by internet standards

| Kind | Safe values | Source |
|------|-------------|--------|
| Email domains | `example.com`, `example.net`, `example.org`, and any domain ending in `.example`, `.test`, or `.invalid` | RFC 2606 and RFC 6761 |
| Website domains | Same as above | RFC 2606 and RFC 6761 |
| IPv4 addresses | `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24` | RFC 5737 (documentation ranges) |
| IPv6 addresses | `2001:db8::/32` | RFC 3849 (documentation range) |

Use `.invalid` when the address must never resolve or receive mail, for
example to test rejection of undeliverable addresses.

## Phone numbers

Some countries set aside number ranges for fiction and testing. Use them
when the market is known:

| Country | Range | Source |
|---------|-------|--------|
| United States and Canada | `555-0100` to `555-0199`, with any area code | North American Numbering Plan administration |
| United Kingdom | Mobile `07700 900000` to `07700 900999`; London `020 7946 0000` to `020 7946 0999` | Ofcom, numbers for drama |

For other countries, check whether the national telecom regulator publishes
such a range, or ask the user for the team's test numbers. If none is
known, say so and use a number that is clearly invalid for the country (for
example too short), labeled as format-only.

## Payment cards

- Use the test card numbers published by the team's payment provider; they
  behave predictably in that provider's test environment (approved,
  declined, needs authentication).
- If the provider is unknown, ask. A widely published generic test number
  such as `4111 1111 1111 1111` may be used for format checks, labeled as a
  generic test number.
- Never generate other numbers that pass the Luhn checksum.
- Expiry dates: a date in the future for valid cards, and a past date for
  expired-card tests. CVC: any three digits, labeled as test values.

## Bank accounts

- Use test accounts or IBANs from the team's bank or payment provider.
- Example IBANs from official standards documentation, such as
  `GB82 WEST 1234 5698 7654 32` and `DE89 3704 0044 0532 0130 00`, are
  widely used in documentation; label them as documentation examples.
- Never generate other checksum-valid account numbers.

## Personal identity numbers

National identity numbers (for example social security or personal
identity numbers) can belong to real people.

- Use test numbers that the issuing authority publishes for testing, where
  they exist, or the team's test numbers. Some tax and population
  authorities publish such lists. Use a published number only if you
  copied it from the list in this session; a remembered number may be
  wrong and could belong to a real person.
- If none is known, ask the user. For a format test, use a value whose
  structure cannot be real (for example an impossible date part), labeled
  as format-only. For a check-digit test, change only the check digit of a
  documented or supplied test number; do not guess a wrong check digit on
  an invented number.
- Never generate checksum-valid identity numbers.

## Names and addresses

- Invent names; combine first and last names freely across cultures, and
  avoid well-known people.
- Real city names and real postal code *formats* are fine. Use invented
  street names, so that no address is a real home.
- Do not pair a real company's name with fake customer data in a way that
  could look like a real record.

## Credentials

- Passwords for test accounts: generate them per run, or use the team's test
  account mechanism. Never reuse a password from the input.
- API keys and tokens: use obvious placeholders such as `TEST-KEY-…`, or the
  provider's documented test keys. Never use a real-looking secret.
