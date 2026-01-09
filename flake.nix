{
  description = "pytest environment";
  
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  };
  
  outputs = { nixpkgs, ... }: {
    devShells.aarch64-darwin.default = 
      let 
        pkgs = nixpkgs.legacyPackages.aarch64-darwin;
        pythonEnv = pkgs.python312.withPackages (ps: with ps; [
          pytest
        ]);
      in pkgs.mkShell {
        packages = with pkgs; [ 
          pythonEnv
        ];
        
        shellHook = ''
        '';
      };
  };
}
