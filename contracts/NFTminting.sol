// This Contract registers digital assets and is automated to approve the transfer of tokens to our market place which are minted on this contract. 

pragma solidity ^0.5.0;

//Iporting open OpenZeppelin ERC721Full

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

// Creating a contract with token name and symbol.

contract mintNFT is ERC721Full {

	address contractAddress;

	constructor(address galleryAddress) public ERC721Full("Cryptic Crusaders", "CRCR1") {
		contractAddress = galleryAddress;
	}

// setting default _tokenId as 0
	uint private _tokenId = 0;

// Creating mintArtwork function

	function mintArtwork(string memory tokenURI) public returns (uint) {
		_tokenId++;
		_mint(msg.sender, _tokenId);
        _setTokenURI(_tokenId, tokenURI);
		setApprovalForAll(contractAddress, true);
		return _tokenId;
	}
}
