/// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

import "./erc_721.sol";

contract saleGallery {
	

	struct createListing {
		address seller;
		address token;
		uint tokenId;
		uint price;
	}

	event tokenListed(
		uint listingId,
		address seller,
		address token,
		uint tokenId,
		uint price
	);

	event tokenSold(
		uint listingId,
		address buyer,
		address token,
		uint tokenId,
		uint price
	);

	event Cancelled(
		uint listingId,
		address seller
	);

	uint private _listingId = 0;
	mapping(uint => createListing) private _listings;

	function listNFT(address token, uint tokenId, uint price) external {
		IERC721(token).transferFrom(msg.sender, address(this), tokenId);

		createListing memory listing = createListing(
			msg.sender,
			token,
			tokenId,
			price
		);

		_listingId++;

		_listings[_listingId] = listing;

		emit tokenListed(
			_listingId,
			msg.sender,
			token,
			tokenId,
			price
		);
	}

	function fetchListing(uint listingId) public view returns (createListing memory) {
		return _listings[listingId];
	}

	function buyToken(uint listingId) external payable {
		createListing storage listing = _listings[listingId];

		require(msg.value >= listing.price, "Non Sufficient Funds");

		IERC721(listing.token).transferFrom(address(this), msg.sender, listing.tokenId);
		payable(listing.seller).transfer(listing.price);

		emit tokenSold(
			listingId,
			msg.sender,
			listing.token,
			listing.tokenId,
			listing.price
		);
	}

	function cancel(uint listingId) public {
		createListing storage listing = _listings[listingId];

		require(msg.sender == listing.seller, "ONLY SELLERS ARE AUTHORIZED TO SELL");
		
	
		IERC721(listing.token).transferFrom(address(this), msg.sender, listing.tokenId);

		emit Cancelled(listingId, listing.seller);
	}
}