Feature: Seer runs ci definition files.

  Scenario: Seer is run on a project without a definition file
     Given seer is available on the path
      when seer is run
      then seer's usage will be output
      """
      usage: seer
      """

  Scenario Outline: Seer is run on a project with a definition file
     Given a <definition_file> present in the project
      """
      script:
      - touch made-by-test
      - ls
      """
      when seer is run
      then the <definition file>'s scripts will be run

    Examples:
     | definition file |
     | seer.yml        |
     | .travis.yml     |
     | ci.yml          |
