import logging


def test_push_single_rhba_advisory_single_build(prepare_single_build, testdata_pub):
    """Use fixture return value in a test."""
    logging.info("[+++] test_push_single_rhba_advisory_single_build is called")

    logging.info("[***] return %s", str(prepare_single_build))

    testdata_pub.login()
    logging.info(
        "[Dry run] Execute pub push_advisory with adv %s",
        str(prepare_single_build["file_list"]),
    )
    # task_id = testdata_pub.push_advisory(
    #     target="target_to_pulp2",
    #     file_list=prepare_single_build["file_list"],
    #     options={},
    #     comment="dichen single_build",
    # )

    # logging.info("[+++] single_build get pub taskid %s", task_id)


def test_push_single_rhsa_advisory_to_published_repos(
    prepare_published_repos, testdata_pub
):
    logging.info("[+++] test_push_single_rhsa_advisory_to_published_repos is called")

    logging.info("[***] return %s", str(prepare_published_repos))

    testdata_pub.login()
    logging.info(
        "[Dry run] Execute pub push_advisory with adv %s",
        str(prepare_published_repos["file_list"]),
    )
    # task_id = testdata_pub.push_advisory(
    #     target="target_to_pulp2",
    #     file_list=prepare_published_repos["file_list"],
    #     options={},
    #     comment="dichen published_repos",
    # )

    # logging.info("[+++] published_repos get pub taskid %s", task_id)
