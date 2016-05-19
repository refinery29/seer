Feature: Seer runs ci definition files.

  Scenario: Seer is run on a project without a definition file
     Given seer is available on the path
      When seer is run
      Then seer's usage will be output
      """
      usage: seer
      """

  Scenario Outline: Seer is run on a project with a script section in its definition file
     Given a <definition_file> present in the project
      """
      script: [ls -A]
      """
      When seer is run
      Then the <definition file>'s scripts will be run
      """
      Running ls -A
      .git
      {{ definition_file }}
      Scripts passed :)
      """

    Examples:
     | definition file |
     | seer.yml        |
     | .travis.yml     |
     | ci.yml          |

  Scenario Outline: Seer is run on a project with a modified section in its definition file
     Given a <definition_file> present in the project
      """
      modified:
        diff: master
        flag_file: flag_file
        script: ls -A
      """
      And a flag file exists in a directory with a modified file
      When seer is run
      Then the <definition file>'s scripts will be run
      """
      Running ls -A
      Running scripts in modified directory {{ modified_dir }}
      flag_file
      Scripts passed :)
      Modified directory scripts passed :)
      """

    Examples:
     | definition file |
     | seer.yml        |
     | .travis.yml     |
     | ci.yml          |
