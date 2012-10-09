from distutils.core import setup

setup(
    name='django-mailbox',
    version='1.2.1',
    url='http://bitbucket.org/latestrevision/django-mailbox/',
    description='Import mail from POP3, IMAP, local mailboxes or directly from Postfix or Exim4 into your Django application automatically.',
    author='Adam Coddington',
    author_email='me@adamcoddington.net',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications :: Email',
        'Topic :: Communications :: Email :: Post-Office',
        'Topic :: Communications :: Email :: Post-Office :: IMAP',
        'Topic :: Communications :: Email :: Post-Office :: POP3',
        'Topic :: Communications :: Email :: Email Clients (MUA)',
    ],
    packages=[
        'django_mailbox',
        'django_mailbox.management',
        'django_mailbox.management.commands',
        'django_mailbox.migrations',
        'django_mailbox.transports',
        ],
)
