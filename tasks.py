import invoke


@invoke.task
def test(ctx):
    ctx.run("nosetests -v")
