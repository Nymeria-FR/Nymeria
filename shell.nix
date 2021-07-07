with import <nixpkgs> { };

let
  nym = python38.withPackages (python-packages:
    with python-packages; [
      discordpy
      pillow
      toml
      python-dotenv

    ]);
in stdenv.mkDerivation {
  name = "nymeria-env";
  buildInputs = [ nym ];
}